from bpy.types import PropertyGroup
from bpy import types as bpy_types

from enum import Enum

from .._register import BlenderTypes
from ..reg_helpers.help_property import PropertyRegister

from ...types import PropertyTypes


class PGRootTypes(Enum):
    WINDOW_MANAGER = bpy_types.WindowManager
    TEMPORAL = WINDOW_MANAGER
    SCENE = bpy_types.Scene

    OBJECT = bpy_types.Object
    MESH = bpy_types.Mesh
    LIGHT = bpy_types.Light
    CAMERA = bpy_types.Camera
    IMAGE = bpy_types.Image
    TEXTURE = bpy_types.Texture
    BRUSH = bpy_types.Brush
    ARMATURE = bpy_types.Armature
    ACTION = bpy_types.Action
    CURVE = bpy_types.Curve
    NODE_TREE = bpy_types.NodeTree
    NODE_GROUP = bpy_types.NodeGroup
    GN_GROUP = bpy_types.GeometryNodeGroup
    SPEAKER = bpy_types.Speaker

    ACTION_GROUP = bpy_types.ActionGroup
    ACTION_GROUPS = bpy_types.ActionGroups
    FCURVE = bpy_types.FCurve
    CURVES = bpy_types.Curves
    MODIFIER = bpy_types.Modifier
    CONSTRAINT = bpy_types.Constraint

    def __call__(self, prop_name: str = None) -> PropertyGroup:
        def decorator(decorated_cls):
            pg_cls = _register_property_group(decorated_cls)
            PropertyRegister(self.value, prop_name if prop_name else 'uvflow', PropertyTypes.POINTER(pg_cls))
            return pg_cls
        return decorator


def _register_property_group(deco_cls) -> PropertyGroup:
    pg_cls = type(
        'UVFLOW_PG_' + deco_cls.__name__,
        (PropertyGroup, deco_cls),
        {
            '__annotations__': deco_cls.__annotations__,
            'bl_label': deco_cls.bl_label if 'bl_label' in deco_cls else deco_cls.__name__,
        }
    )
    BlenderTypes.PropertyGroup.add_class(pg_cls)
    return pg_cls


##########################################################################
##########################################################################
# enum-like-class UTILITY TO REGISTER PROPERTY GROUP CLASSES PER TYPE.
##########################################################################

class PropertyGroupRegister:
    # PropertyGroup added to a root type like Scene, WindowManager or any ID (PG supported) type.
    ROOT = PGRootTypes
    # Child of another PropertyGroup.
    CHILD = _register_property_group
