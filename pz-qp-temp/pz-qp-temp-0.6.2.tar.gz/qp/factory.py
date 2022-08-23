"""This module implements a factory that manages different types of PDFs"""

import sys
import os

from collections import OrderedDict

import numpy as np

from scipy import stats as sps

from tables_io import io
from tables_io.types import NUMPY_DICT

from qp.ensemble import Ensemble

from qp.dict_utils import compare_dicts, concatenate_dicts

from qp.pdf_gen import Pdf_gen_wrap


class Factory(OrderedDict):
    """Factory that creates and mangages PDFs

    """
    def __init__(self):
        """C'tor"""
        super(Factory, self).__init__()
        self._load_scipy_classes()

    @staticmethod
    def _build_data_dict(md_table, data_table):
        """Convert the tables to a dictionary that can be used to build an Ensemble"""
        data_dict = {}

        for col, col_data in md_table.items():

            ndim = np.ndim(col_data)

            if ndim > 1:
                col_data = np.squeeze(col_data)
                if np.ndim(col_data) == 0:
                    col_data = col_data.item()
            elif ndim == 1:
                col_data = col_data[0]

            if isinstance(col_data, bytes):
                col_data = col_data.decode()

            data_dict[col] = col_data

        for col, col_data in data_table.items():
            if len(col_data.shape) < 2: #pragma: no cover
                data_dict[col] = np.expand_dims(col_data, -1)
            else:
                data_dict[col] = col_data
        return data_dict

    def _make_scipy_wrapped_class(self, class_name, scipy_class):
        """Build a qp class from a scipy class"""
        # pylint: disable=protected-access
        override_dict = dict(name=class_name,
                                version=0,
                                freeze=Pdf_gen_wrap._my_freeze,
                                _argcheck=Pdf_gen_wrap._my_argcheck,
                                _other_argcheck=scipy_class._argcheck,
                                _other_init=scipy_class.__init__)
        the_class = type(class_name, (Pdf_gen_wrap, scipy_class), override_dict)
        self.add_class(the_class)

    def _load_scipy_classes(self):
        """Build qp classes from all the scipy classes"""
        names = sps.__all__
        for name in names:
            attr = getattr(sps, name)
            if isinstance(attr, sps.rv_continuous):
                self._make_scipy_wrapped_class(name, type(attr))

    def add_class(self, the_class):
        """Add a class to the factory

        Parameters
        ----------
        the_class : class
            The class we are adding, must inherit from Pdf_Gen
        """
        #if not isinstance(the_class, Pdf_gen): #pragma: no cover
        #    raise TypeError("Can only add sub-classes of Pdf_Gen to factory")
        if not hasattr(the_class, 'name'): #pragma: no cover
            raise AttributeError("Can not add class %s to factory because it doesn't have a name attribute" % the_class)
        if the_class.name in self: #pragma: no cover
            raise KeyError("Class nameed %s is already in factory, point to %s" % (the_class.name, self[the_class.name]))
        the_class.add_method_dicts()
        the_class.add_mappings()
        self[the_class.name] = the_class
        setattr(self, "%s_gen" % the_class.name, the_class)
        setattr(self, the_class.name, the_class.create)


    def create(self, class_name, data, method=None):
        """Make an ensemble of a particular type of distribution

        Parameters
        ----------
        class_name : `str`
            The name of the class to make
        data : `dict`
            Values passed to class create function
        method : `str` [`None`]
            Used to select which creation method to invoke

        Returns
        -------
        ens : `qp.Ensemble`
            The newly created ensemble
        """
        if class_name not in self: #pragma: no cover
            raise KeyError("Class nameed %s is not in factory" % class_name)
        the_class = self[class_name]
        ctor_func = the_class.creation_method(method)
        return Ensemble(ctor_func, data)


    def read(self, filename):
        """Read this ensemble from a file

        Parameters
        ----------
        filename : `str`

        Notes
        -----
        This will actually read two files, one for the metadata and one for the object data

        This will use information in the meta data to figure out how to construct the data
        need to build the ensemble.
        """
        _, ext = os.path.splitext(filename)
        if ext in ['.pq']:
            keys = ['data', 'meta', 'ancil']
            allow_missing_keys = True
        else:
            keys = None
            allow_missing_keys = False

        tables = io.read(filename, NUMPY_DICT, keys=keys,
                         allow_missing_keys=allow_missing_keys) #pylint: disable=no-member

        md_table = tables['meta']
        data_table = tables['data']
        ancil_table = tables.get('ancil')

        data = self._build_data_dict(md_table, data_table)

        pdf_name = data.pop('pdf_name')
        pdf_version = data.pop('pdf_version')
        if pdf_name not in self: #pragma: no cover
            raise KeyError("Class nameed %s is not in factory" % pdf_name)

        the_class = self[pdf_name]
        reader_convert = the_class.reader_method(pdf_version)
        ctor_func = the_class.creation_method(None)
        if reader_convert is not None: #pragma: no cover
            data = reader_convert(data)
        return Ensemble(ctor_func, data=data, ancil=ancil_table)


    def convert(self, in_dist, class_name, **kwds):
        """Read an ensemble to a different repersenation

        Parameters
        ----------
        in_dist : `qp.Ensemble`
            Input distributions
        class_name : `str`
            Representation to convert to

        Returns
        -------
        ens : `qp.Ensemble`
            The ensemble we converted to
        """
        kwds_copy = kwds.copy()
        method = kwds_copy.pop("method", None)
        if class_name not in self: #pragma: no cover
            raise KeyError("Class nameed %s is not in factory" % class_name)
        if class_name not in self: #pragma: no cover
            raise KeyError("Class nameed %s is not in factory" % class_name)
        the_class = self[class_name]
        extract_func = the_class.extraction_method(method)
        if extract_func is None: #pragma: no cover
            raise KeyError("Class named %s does not have a extraction_method named %s" % (class_name, method))
        data = extract_func(in_dist, **kwds_copy)
        return self.create(class_name, data, method)


    def pretty_print(self, stream=sys.stdout):
        """Print a level of the converstion dictionary in a human-readable format

        Parameters
        ----------
        stream : `stream`
            The stream to print to
        """
        for class_name, cl in self.items():
            stream.write("\n")
            stream.write("%s: %s\n" % (class_name, cl))
            cl.print_method_maps(stream)

    @staticmethod
    def concatenate(ensembles):
        """Concatanate a list of ensembles

        Parameters
        ----------
        ensembles : `list`
            The ensembles we are concatanating

        Returns
        -------
        ens : `qp.Ensemble`
            The output
        """
        if not ensembles:  #pragma: no cover
            return None
        metadata_list = []
        objdata_list = []
        ancil_list = []
        gen_func = None
        for ensemble in ensembles:
            metadata_list.append(ensemble.metadata())
            objdata_list.append(ensemble.objdata())
            if gen_func is None:
                gen_func = ensemble.gen_func
            if ancil_list is not None:
                if ensemble.ancil is None:
                    ancil_list = None
                else:  #pragma: no cover
                    ancil_list.append(ensemble.ancil)
        if not compare_dicts(metadata_list):  #pragma: no cover
            raise ValueError("Metadata does not match")
        metadata = metadata_list[0]
        data = concatenate_dicts(objdata_list)
        if ancil_list is not None:  #pragma: no cover
            ancil = concatenate_dicts(ancil_list)
        else:
            ancil = None
        for k, v in metadata.items():
            if k in ['pdf_name', 'pdf_version']:
                continue
            data[k] = np.squeeze(v)
        return Ensemble(gen_func, data, ancil)


_FACTORY = Factory()

def instance():
    """Return the factory instance"""
    return _FACTORY

stats = _FACTORY
add_class = _FACTORY.add_class
create = _FACTORY.create
read = _FACTORY.read
convert = _FACTORY.convert
concatenate = _FACTORY.concatenate
