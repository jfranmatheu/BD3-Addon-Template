from ._addon_info import AddonInfo # Use this in your __init__.py file to create the bl_info object.
from ._auto_load import AutoLoad # Use this in your __init__.py file to initialize and automate the addon registration. (see 'AutoLoad.magic()')
from ._globals import GLOBALS # Common Global Variables that can be used in your addon.

from bpy import types as btypes # Blender Types.
from ._register import Reg, OpsReturn

from .types import PropertyTypes as Property, EventValue, EventType, Mouse, RegionType, SpaceType


'''
Usually you would use:
- RegType
    > Addon Types to register b3d classes that inherit from these types.
    > to register Operator, AddonPreferences and Panel/Menu (UI) classes.
- RegDeco
    > Addon Decorators to register b3d classes that are decorated with these decorators.
    > to register PropertyGroup classes as well as UI appends to other UI classes (including builtin classes).
'''
