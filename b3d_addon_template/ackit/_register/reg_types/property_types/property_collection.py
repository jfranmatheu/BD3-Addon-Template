from bpy.props import *
from bpy import types as bpy_types

from enum import Enum


# TODO: # Not implemented yet. Should create an empty collection with a pointer of the selected type.

class CollectionPropertyHelper(Enum):
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

    def __call__(self, name: str, **kwargs: dict) -> bpy_types.CollectionProperty:
        if self.value is None:
            if 'type' not in kwargs:
                raise AttributeError("'type' kwarg must be specified to create a - CUSTOM - CollectionProperty")
            return CollectionProperty(name=name, **kwargs)
        return CollectionProperty(type=self.value, name=name, **kwargs)
