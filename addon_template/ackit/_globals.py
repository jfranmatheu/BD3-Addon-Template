import bpy
import sys
from pathlib import Path

from .. import __package__ as __main_package__#, bl_info


def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None


class GLOBALS:
    PYTHON_PATH = sys.executable

    BLENDER_VERSION = bpy.app.version
    IN_BACKGROUND = bpy.app.background

    ADDON_MODULE = __main_package__
    ADDON_SOURCE_PATH = Path(__file__).parent.parent
    #ADDON_NAME = bl_info['name']
    #ADDON_VERSION = bl_info['version']
    #SUPPORTED_BLENDER_VERSION = bl_info['blender']

    IN_DEVELOPMENT = debugger_is_active() # Just a nice HACK! ;-)
    IN_PRODUCTION  = not IN_DEVELOPMENT


    class CodeGen:
        TYPES = 'types.py'
        ICONS = 'icons.py'
        OPS = 'ops.py'
