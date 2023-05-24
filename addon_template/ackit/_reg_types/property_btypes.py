from .. import btypes
from enum import Enum


class PropertyBpyTypes(Enum):
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


def get_property_bpy_types():
    return compile('\t\n'.join([f'{btype.name} = {btype.value}' for btype in PropertyBpyTypes]))
