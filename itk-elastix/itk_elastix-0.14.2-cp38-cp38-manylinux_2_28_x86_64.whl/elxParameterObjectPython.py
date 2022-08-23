# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _ElastixPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _elxParameterObjectPython
else:
    import _elxParameterObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _elxParameterObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _elxParameterObjectPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
class mapstringvectorstring(collections.abc.MutableMapping):
    r"""Proxy of C++ std::map< std::string,std::vector< std::string > > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___nonzero__)
    __bool__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___bool__)
    __len__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___len__)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()
    __getitem__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___getitem__)
    __delitem__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___delitem__)
    has_key = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_has_key)
    keys = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_keys)
    values = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_values)
    items = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_items)
    __contains__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___contains__)
    key_iterator = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_key_iterator)
    value_iterator = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_value_iterator)
    __setitem__ = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring___setitem__)
    asdict = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_asdict)

    def __init__(self, *args):
        r"""
        __init__(self, other) -> mapstringvectorstring

        Parameters
        ----------
        other: std::less< std::string > const &

        __init__(self) -> mapstringvectorstring
        __init__(self, other) -> mapstringvectorstring

        Parameters
        ----------
        other: std::map< std::string,std::vector< std::string,std::allocator< std::string > > > const &

        """
        _elxParameterObjectPython.mapstringvectorstring_swiginit(self, _elxParameterObjectPython.new_mapstringvectorstring(*args))
    empty = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_empty)
    size = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_size)
    swap = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_swap)
    begin = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_begin)
    end = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_end)
    rbegin = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_rbegin)
    rend = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_rend)
    clear = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_clear)
    get_allocator = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_get_allocator)
    count = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_count)
    erase = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_erase)
    find = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_find)
    lower_bound = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_lower_bound)
    upper_bound = _swig_new_instance_method(_elxParameterObjectPython.mapstringvectorstring_upper_bound)
    __swig_destroy__ = _elxParameterObjectPython.delete_mapstringvectorstring

# Register mapstringvectorstring in _elxParameterObjectPython:
_elxParameterObjectPython.mapstringvectorstring_swigregister(mapstringvectorstring)


def elastixParameterObject_New():
    return elastixParameterObject.New()

class elastixParameterObject(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ elastixParameterObject class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_elxParameterObjectPython.elastixParameterObject___New_orig__)
    Clone = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_Clone)
    SetParameterMap = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_SetParameterMap)
    AddParameterMap = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_AddParameterMap)
    GetParameterMap = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_GetParameterMap)
    GetNumberOfParameterMaps = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_GetNumberOfParameterMaps)
    SetParameter = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_SetParameter)
    GetParameter = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_GetParameter)
    RemoveParameter = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_RemoveParameter)
    ReadParameterFile = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_ReadParameterFile)
    AddParameterFile = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_AddParameterFile)
    WriteParameterFile = _swig_new_instance_method(_elxParameterObjectPython.elastixParameterObject_WriteParameterFile)
    GetDefaultParameterMap = _swig_new_static_method(_elxParameterObjectPython.elastixParameterObject_GetDefaultParameterMap)

    def __init__(self):
        r"""__init__(self) -> elastixParameterObject"""
        _elxParameterObjectPython.elastixParameterObject_swiginit(self, _elxParameterObjectPython.new_elastixParameterObject())
    __swig_destroy__ = _elxParameterObjectPython.delete_elastixParameterObject
    cast = _swig_new_static_method(_elxParameterObjectPython.elastixParameterObject_cast)

    def New(*args, **kargs):
        """New() -> elastixParameterObject

        Create a new object of the class elastixParameterObject and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          elastixParameterObject.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = elastixParameterObject.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = elastixParameterObject.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register elastixParameterObject in _elxParameterObjectPython:
_elxParameterObjectPython.elastixParameterObject_swigregister(elastixParameterObject)
elastixParameterObject___New_orig__ = _elxParameterObjectPython.elastixParameterObject___New_orig__
elastixParameterObject_GetDefaultParameterMap = _elxParameterObjectPython.elastixParameterObject_GetDefaultParameterMap
elastixParameterObject_cast = _elxParameterObjectPython.elastixParameterObject_cast



