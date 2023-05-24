from bpy.props import *
from .. import btypes
from .property_btypes import PropertyBpyTypes, get_property_bpy_types

from enum import Enum


class CollectionPropertyTypes(Enum):
    get_property_bpy_types()

    def __call__(self, name: str, **kwargs: dict) -> btypes.CollectionProperty:
        if self.value is None:
            if 'type' not in kwargs:
                raise AttributeError("'type' kwarg must be specified to create a - CUSTOM - PointerProperty")
            return CollectionProperty(name=name, **kwargs)
        return CollectionProperty(type=self.value, name=name, **kwargs)

CollectionPropertyTypes.ARMATURE()
