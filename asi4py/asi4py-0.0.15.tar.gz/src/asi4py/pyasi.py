from ctypes import cdll, CDLL, RTLD_GLOBAL
from ctypes import POINTER, byref, c_int, c_int64, c_int32, c_bool, c_char_p, c_double, c_void_p, CFUNCTYPE, py_object, cast, byref
import ctypes

'''
CDLL(MPI.__file__, mode=RTLD_GLOBAL) is a workaround for a few MPICH bugs, including 
the bug with non-working MPI_IN_PLACE and 2-stage ELPA solver
https://bitbucket.org/mpi4py/mpi4py/issues/162/mpi4py-initialization-breaks-fortran
https://lists.mpich.org/pipermail/discuss/2020-July/006018.html
'''
from mpi4py import MPI
CDLL(MPI.__file__, mode=RTLD_GLOBAL)

import numpy as np
from numpy.ctypeslib import ndpointer

import sys
from pathlib import Path
import os, shutil
from ase import units
from scalapack4py import ScaLAPACK4py

libdl = cdll.LoadLibrary('libdl.so')
dmhs_callback = CFUNCTYPE(None, c_void_p, c_int, c_int, POINTER(c_int), POINTER(c_double))  # void(*)(void *aux_ptr, int iK, int iS, int *blacs_descr, void *blacs_data)
esp_callback = CFUNCTYPE(None, c_void_p, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double))   # void(*)(void *aux_ptr, int n, const double *coords, double *potential, double *potential_grad)

def default_saving_callback(aux, iK, iS, descr, data):
  try:
    asi, storage_dict, label = cast(aux, py_object).value
    data = asi.scalapack.gather_numpy(descr, data, (asi.n_basis,asi.n_basis))
    if data is not None:
      storage_dict[(iK, iS)] = data.copy()
  except Exception as eee:
    print (f"Something happened in ASI default_saving_callback {label}: {eee}\nAborting...")
    MPI.COMM_WORLD.Abort(1)

def default_loading_callback(aux, iK, iS, descr, data):
  try:
    asi, storage_dict, label = cast(aux, py_object).value
    m = storage_dict[(iK, iS)] if asi.scalapack.is_root(descr) else None
    assert m is None or (asi.n_basis == m.shape[0]) and (asi.n_basis == m.shape[1]), \
                     f"m.shape=={m.shape} != asi.n_basis=={asi.n_basis}"
    asi.scalapack.scatter_numpy(m, descr, data)
  except Exception as eee:
    print (f"Something happened in ASI default_loading_callback {label}: {eee}\nAborting...")
    MPI.COMM_WORLD.Abort(1)

class ASIlib:
  def __init__(self, lib_file, initializer, mpi_comm=None, atoms=None, work_dir='asi.temp', logfile='asi.log'):
    self.lib_file = Path(lib_file).resolve()
    self.initializer = initializer
    if mpi_comm is not None:
      self.mpi_comm = mpi_comm
    else:
      from mpi4py import MPI
      self.mpi_comm = MPI.COMM_WORLD
    self.atoms = atoms.copy() if atoms is not None else None
    self.work_dir = Path(work_dir)
    self.work_dir.mkdir(parents=True, exist_ok=True)
    self.logfile = logfile

  def __enter__(self):
    return self.init()

  def __exit__(self, type, value, traceback):
    #Exception handling here
    #print ("__exit__: ", type, value, traceback)
    self.close()  

  def init(self):
    curdir = os.getcwd()
    try:
      os.chdir(self.work_dir)
      
      if self.mpi_comm.Get_rank() == 0:
        self.initializer(self)
    
      # Load the FHI-aims library
      # mode=RTLD_GLOBAL is necessary to get rid of the error with MKL:
      # 		`INTEL MKL ERROR: /opt/intel/oneapi/mkl/2021.4.0/lib/intel64/libmkl_avx512.so.1: undefined symbol: mkl_sparse_optimize_bsr_trsm_i8.`
      # Details: https://bugs.launchpad.net/ubuntu/+source/intel-mkl/+bug/1947626
      self.lib = CDLL(self.lib_file, mode=RTLD_GLOBAL)
      self.scalapack = ScaLAPACK4py(self.lib)

      self.lib.ASI_n_atoms.restype = c_int
      self.lib.ASI_energy.restype = c_double
      self.lib.ASI_forces.restype = POINTER(c_double)
      self.lib.ASI_atomic_charges.restype = POINTER(c_double)
      self.lib.ASI_atomic_charges.argtypes  = [c_int,]
      self.lib.ASI_calc_esp.argtypes = [c_int, ndpointer(dtype=np.float64), ndpointer(dtype=np.float64), ndpointer(dtype=np.float64)]
      self.lib.ASI_register_dm_callback.argtypes = [dmhs_callback, c_void_p]
      self.lib.ASI_register_overlap_callback.argtypes = [dmhs_callback, c_void_p]
      self.lib.ASI_register_hamiltonian_callback.argtypes = [dmhs_callback, c_void_p]
      if hasattr(self.lib, "ASI_register_dm_init_callback"):
        self.lib.ASI_register_dm_init_callback.argtypes = [dmhs_callback, c_void_p]
      self.lib.ASI_register_external_potential.argtypes = [esp_callback, c_void_p];
      self.lib.ASI_is_hamiltonian_real.restype = c_bool
      self.lib.ASI_get_basis_size.restype = c_int
      self.lib.ASI_get_nspin.restype = c_int
      self.lib.ASI_get_nkpts.restype = c_int
      self.lib.ASI_get_n_local_ks.restype = c_int
      self.lib.ASI_get_local_ks.restype = c_int
      self.lib.ASI_get_local_ks.argtypes = [ndpointer(dtype=np.int32),]
      self.lib.ASI_is_hamiltonian_real.restype = c_bool
      
      input_filename = {1:"dummy", 2:"dftb_in.hsd"}[self.lib.ASI_flavour()]
      self.lib.ASI_init(input_filename.encode('UTF-8'), self.logfile.encode('UTF-8'), c_int(self.mpi_comm.py2f()))
      if (self.lib.ASI_flavour() == 2):
        self.set_coords() # FIXME
      return self
    finally:
      os.chdir(curdir)
  
  def close(self):
    curdir = os.getcwd()
    try:
      os.chdir(self.work_dir)
      self.lib.ASI_finalize()
      handle = self.lib._handle
      del self.lib
      if self.mpi_comm.Get_rank() == 0:
        os.system(f"cat {self.logfile} >> total.log")
    finally:
      os.chdir(curdir)
    
  def run(self):
    curdir = os.getcwd()
    try:
      os.chdir(self.work_dir)
      self.lib.ASI_run()
    finally:
      os.chdir(curdir)

  def register_DM_init(self, dm_init_callback, dm_init_aux):
    self.dm_init_callback = dmhs_callback(dm_init_callback)
    self.dm_init_aux = dm_init_aux
    self.lib.ASI_register_dm_init_callback(self.dm_init_callback, c_void_p.from_buffer(py_object(self.dm_init_aux)))

  def register_overlap_callback(self, overlap_callback, overlap_aux):
    self.overlap_callback = dmhs_callback(overlap_callback)
    self.overlap_aux = overlap_aux
    self.lib.ASI_register_overlap_callback(self.overlap_callback, c_void_p.from_buffer(py_object(self.overlap_aux)))

  def register_hamiltonian_callback(self, hamiltonian_callback, hamiltonian_aux):
    self.hamiltonian_callback = dmhs_callback(hamiltonian_callback)
    self.hamiltonian_aux = hamiltonian_aux
    self.lib.ASI_register_hamiltonian_callback(self.hamiltonian_callback, c_void_p.from_buffer(py_object(self.hamiltonian_aux)))

  def register_dm_callback(self, dm_callback, dm_aux):
    self.dm_callback = dmhs_callback(dm_callback)
    self.dm_aux = dm_aux
    self.lib.ASI_register_dm_callback(self.dm_callback, c_void_p.from_buffer(py_object(self.dm_aux)))

  def register_external_potential(self, ext_pot_func, ext_pot_aux_obj):
    '''
      self.ext_pot_func returns potential for positive charges
    '''
    self.ext_pot_func = esp_callback(ext_pot_func)
    self.ext_pot_aux_obj = ext_pot_aux_obj
    self.lib.ASI_register_external_potential(self.ext_pot_func, c_void_p.from_buffer(py_object(self.ext_pot_aux_obj)))

  def calc_esp(self, coords):
    n = len(coords)
    esp = np.zeros((n,), dtype=c_double)
    esp_grad = np.zeros((n,3), dtype=c_double)
    self.lib.ASI_calc_esp(c_int(n), coords.ravel(), esp, esp_grad) 
    return esp, esp_grad

  @property
  def n_atoms(self):
    return self.lib.ASI_n_atoms()

  @property
  def n_basis(self):
    return self.lib.ASI_get_basis_size()

  @property
  def n_spin(self):
    return self.lib.ASI_get_nspin()

  @property
  def n_kpts(self):
    return self.lib.ASI_get_nkpts()

  @property
  def n_local_ks(self):
    return self.lib.ASI_get_n_local_ks()

  @property
  def local_ks(self):
    n = self.n_local_ks
    res = np.zeros((n*2,), dtype=c_int32)
    n2 =  self.lib.ASI_get_local_ks(res)
    assert n == n2
    return res

  @property
  def is_hamiltonian_real(self):
    return self.lib.ASI_is_hamiltonian_real()

  @property
  def total_forces(self):
    forces_ptr = self.lib.ASI_forces()
    if forces_ptr:
      return np.ctypeslib.as_array(forces_ptr, shape=(self.n_atoms, 3))
    else:
      return None

  @property
  def atomic_charges(self):
    chg_ptr = self.lib.ASI_atomic_charges(-1)
    if chg_ptr:
      return np.ctypeslib.as_array(chg_ptr, shape=(self.n_atoms,)).copy()
    else:
      return None

  @property
  def total_energy(self):
    return self.lib.ASI_energy()
  
  def set_coords(self, coords=None):
    if coords is not None:
      assert False
      self.atoms.positions[:] = coords
    self.lib.ASI_set_atom_coords((self.atoms.positions / units.Bohr).ctypes.data_as(c_void_p), len(self.atoms))
    
  @property
  def is_eigen_real(self):
    return self.lib.ASI_is_hamiltonian_real()
  
  @property
  def keep_density_matrix(self):
    return hasattr(self, 'dm_callback')

  @keep_density_matrix.setter
  def keep_density_matrix(self, value):
    assert (value, 'callback unsetting not implemented')
    if self.keep_density_matrix:
      return

    self.dm_storage = {}
    self.register_dm_callback(default_saving_callback, (self, self.dm_storage, 'DM calc'))

  @property
  def init_density_matrix(self):
    return hasattr(self, 'dm_init_callback')
 
  @init_density_matrix.setter
  def init_density_matrix(self, value):
    self.dm_init_storage = value
    self.register_DM_init(default_loading_callback, (self, self.dm_init_storage, 'DM init'))

