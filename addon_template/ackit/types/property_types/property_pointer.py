from bpy.props import *
from .. import btypes
from ._btypes import PropertyBpyTypes

from enum import Enum


class PointerPropertyTypes(Enum, PropertyBpyTypes):
    def __call__(self, name: str, **kwargs: dict) -> btypes.PointerProperty:
        if self.value is None:
            if 'type' not in kwargs:
                raise AttributeError("'type' kwarg must be specified to create a - CUSTOM - PointerProperty")
            return PointerProperty(name=name, **kwargs)
        return PointerProperty(type=self.value, name=name, **kwargs)
