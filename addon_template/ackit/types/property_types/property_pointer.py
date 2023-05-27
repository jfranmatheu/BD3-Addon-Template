from bpy.props import *
from bpy import types as btypes

from ._btypes import PropertyBpyTypes

from enum import Enum


class PointerPropertyTypes(Enum):
    OBJECT = btypes.Object
    MESH = btypes.Mesh
    CAMERA = btypes.Camera
    LIGHT = btypes.Light
    ARMATURE = btypes.Armature
    NODE_TREE = btypes.NodeTree
    NODE_GROUP = btypes.NodeGroup
    BRUSH = btypes.Brush
    IMAGE = btypes.Image
    TEXTURE = btypes.Texture
    CUSTOM = None

    def __call__(self, name: str, **kwargs: dict) -> btypes.PointerProperty:
        if self.value is None:
            if 'type' not in kwargs:
                raise AttributeError("'type' kwarg must be specified to create a - CUSTOM - PointerProperty")
            return PointerProperty(name=name, **kwargs)
        return PointerProperty(type=self.value, name=name, **kwargs)
