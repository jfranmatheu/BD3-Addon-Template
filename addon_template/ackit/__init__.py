from ._addon_info import AddonInfo # Use this in your __init__.py file to create the bl_info object.
from ._auto_load import AutoLoad # Use this in your __init__.py file to initialize and automate the addon registration. (see 'AutoLoad.magic()')
from ._globals import GLOBALS # Common Global Variables that can be used in your addon.

from bpy import types as btypes # Blender Types.
from ._reg_types import RegType, Property # Addon Types to register b3d classes that inherit from these types. Also properties.
from ._reg_decorators import RegDeco # Addon Decorators to register b3d classes that are decorated with these decorators.


'''
Usually you would use:
- RegType > to register Operator, AddonPreferences and Panel/Menu (UI) classes.
- RegDeco > to register PropertyGroup classes as well as UI appends to other UI classes (including builtin classes).
'''
