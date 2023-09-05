import bpy
import sys
from pathlib import Path
import pprint

from .. import __package__ as __main_package__#, bl_info


class GLOBALS:
    PYTHON_PATH = sys.executable

    BLENDER_VERSION = bpy.app.version
    IN_BACKGROUND = bpy.app.background

    ADDON_MODULE = __main_package__
    ADDON_SOURCE_PATH = Path(__file__).parent.parent
    #ADDON_NAME = bl_info['name']
    #ADDON_VERSION = bl_info['version']
    #SUPPORTED_BLENDER_VERSION = bl_info['blender']

    IN_DEVELOPMENT = hasattr(sys, 'gettrace') and sys.gettrace() is not None # Just a nice HACK! ;-)
    IN_PRODUCTION  = not IN_DEVELOPMENT


    class CodeGen:
        TYPES = 'types.py'
        ICONS = 'icons.py'
        OPS = 'ops.py'


def print_debug(*args) -> None:
    if GLOBALS.IN_DEVELOPMENT:
        print(f'[{GLOBALS.ADDON_MODULE.upper()}]', *args)


def pprint_debug(title: str, d: dict, sort: bool = False) -> None:
    if GLOBALS.IN_DEVELOPMENT:
        print_debug('\n+++', title, '++++++++++++++++++++++++++++++++')
        pprint.pprint(d, indent=4, sort_dicts=sort)
        print_debug('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


class CM_PrintDebug:
    def __init__(self, title: str) -> None:
        self.use_debug = GLOBALS.IN_DEVELOPMENT
        if self.use_debug:
            print_debug('\n---', title, '----------------------------')

    def __enter__(self):
        def print_indent(msg: str, indent: int = 1, prefix: str = '>'):
            if self.use_debug:
                t_char = '\t'
                print(f"{''.join([t_char for i in range(indent)])}{prefix} {msg}")
        return print_indent

    def __exit__(self, exc_type, exc_value, trace):
        print_debug('----------------------------------------------------------------------------\n')
