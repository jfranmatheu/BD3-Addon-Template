from ._addon_info import AddonInfo # Use this in your __init__.py file to create the bl_info object.
from ._auto_load import AutoLoad # Use this in your __init__.py file to initialize and automate the addon registration. (see 'AutoLoad.magic()')
from ._globals import GLOBALS # Common Global Variables that can be used in your addon.

# BPY.
from bpy import types as bpy_types, props as bpy_props, ops as bpy_ops # Blender Types.

# ACKit.
from . import types
from ._register import (
    Reg,
    RegType as ack_types,
    RegDeco as ack_deco,
    RegHelper as ack_helper,
    PropertyTypes,
)
from .types.operator import OpsReturn
from .context_manager import ACK_CM


class ACK:
    CM = ACK_CM
    Register = Reg
