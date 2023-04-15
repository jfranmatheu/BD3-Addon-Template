import bpy
import sys

from .. import __package__ as __main_package__
from .. import bl_info


class GLOBALS:
    PYTHON_PATH = sys.executable

    BLENDER_VERSION = bpy.app.version
    IN_BACKGROUND = bpy.app.background

    ADDON_MODULE = __main_package__
    ADDON_NAME = bl_info['name']
    ADDON_VERSION = bl_info['version']
    SUPPORTED_BLENDER_VERSION = bl_info['blender']
