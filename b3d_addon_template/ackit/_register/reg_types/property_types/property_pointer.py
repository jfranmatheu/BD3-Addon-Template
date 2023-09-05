from bpy.props import *
from bpy import types as bpy_types

from enum import Enum


class PointerPropertyTypes(Enum):
    OBJECT = bpy_types.Object
    MESH = bpy_types.Mesh
    CAMERA = bpy_types.Camera
    LIGHT = bpy_types.Light
    ARMATURE = bpy_types.Armature
    NODE_TREE = bpy_types.NodeTree
    NODE_GROUP = bpy_types.NodeGroup
    BRUSH = bpy_types.Brush
    IMAGE = bpy_types.Image
    TEXTURE = bpy_types.Texture
    CUSTOM = None

    def __call__(self, name: str, **kwargs: dict) -> bpy_types.PointerProperty:
        if self.value is None:
            if 'type' not in kwargs:
                raise AttributeError("'type' kwarg must be specified to create a - CUSTOM - PointerProperty")
            return PointerProperty(name=name, **kwargs)
        return PointerProperty(type=self.value, name=name, **kwargs)
