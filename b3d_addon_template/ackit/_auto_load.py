import importlib
import pkgutil
import typing
import inspect
import pathlib
import sys

import bpy

from ._globals import GLOBALS

modules = None
registered = False


class AutoLoad:
    ''' Add this to your main __init__.py
        Usage:
            AutoLoad.set_info()
            AutoLoad.initialize()
        Usage if using own register and unregister in main __init__.py
        Include these in your register() and unregister():
            AutoLoad._register()
            AutoLoad._unregister()
    '''

    @classmethod
    def initialize(cls, works_in_background: bool = False):
        main_module = importlib.import_module(GLOBALS.ADDON_MODULE)

        if hasattr(main_module, 'register'):
            return

        if not works_in_background and bpy.app.background:
            main_module.register = lambda: None
            main_module.unregister = lambda: None

        else:
            main_module.register = cls._register_modules
            main_module.unregister = cls._unregister_modules

            cls._init_modules()

        importlib.reload(main_module)

    magic = initialize

    @classmethod
    def _init_modules(cls):
        global modules
        global registered

        if modules is not None:
            cls._cleanse_modules()

        modules = get_all_submodules(pathlib.Path(__file__).parent.parent)
        # registered = False

        if registered:
            return

        for module in modules:
            # When you need to initialize something specific in this module.
            if hasattr(module, "init"):
                module.init()

        for module in modules:
            # When you need to initialize something that depends on another module initialization.
            if hasattr(module, "late_init"):
                module.late_init()

    @classmethod
    def _cleanse_modules(cls):
        global modules

        sys_modules = sys.modules
        for module in modules:
            if module in sys_modules:
                del sys.modules[module.__name__]

    @classmethod
    def _register_modules(cls):
        global registered
        global modules
        if modules is None:
            cls._init_modules()
        if registered:
            return
        for module in modules:
            if hasattr(module, "register"):
                module.register()
        for module in modules:
            if hasattr(module, "late_register"):
                module.late_register()
        registered = True

    @classmethod
    def _unregister_modules(cls):
        global modules
        global registered
        if not registered:
            return
        for module in modules:
            if hasattr(module, "unregister"):
                module.unregister()
        for module in modules:
            if hasattr(module, "late_unregister"):
                module.late_unregister()
        registered = False

LoadAddon = AutoLoad.magic

###############################################
# ADDON MODULES INITIALIZATION UTIL FUNCTIONS #
###############################################

# Import modules
#################################################

def get_all_submodules(directory):
    return list(iter_submodules(directory, directory.name))

def iter_submodules(path, package_name):
    for name in sorted(iter_submodule_names(path)):
        yield importlib.import_module("." + name, package_name)

def iter_submodule_names(path, root=""):
    for _, module_name, is_package in pkgutil.iter_modules([str(path)]):
        if is_package:
            sub_path = path / module_name
            sub_root = root + module_name + "."
            yield from iter_submodule_names(sub_path, sub_root)
        else:
            yield root + module_name


# Find classes to register
#################################################

def get_ordered_pg_classes_to_register(classes) -> list:
    my_classes = set(classes)
    my_classes_by_idname = {cls.bl_idname : cls for cls in classes if hasattr(cls, "bl_idname")}

    deps_dict = {}
    for cls in my_classes:
        deps_dict[cls] = set(iter_my_register_deps(cls, my_classes, my_classes_by_idname))

    return toposort(deps_dict)

def get_ordered_classes_to_register(modules):
    return toposort(get_register_deps_dict(modules))

def get_register_deps_dict(modules):
    my_classes = set(iter_my_classes(modules))
    my_classes_by_idname = {cls.bl_idname : cls for cls in my_classes if hasattr(cls, "bl_idname")}

    deps_dict = {}
    for cls in my_classes:
        deps_dict[cls] = set(iter_my_register_deps(cls, my_classes, my_classes_by_idname))
    return deps_dict

def iter_my_register_deps(cls, my_classes, my_classes_by_idname):
    yield from iter_my_deps_from_annotations(cls, my_classes)
    yield from iter_my_deps_from_parent_id(cls, my_classes_by_idname)

def iter_my_deps_from_annotations(cls, my_classes):
    for value in typing.get_type_hints(cls, {}, {}).values():
        dependency = get_dependency_from_annotation(value)
        if dependency is not None:
            if dependency in my_classes:
                yield dependency

def get_dependency_from_annotation(value):
    if GLOBALS.BLENDER_VERSION >= (2, 93):
        if isinstance(value, bpy.props._PropertyDeferred):
            return value.keywords.get("type")
    else:
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] in (bpy.props.PointerProperty, bpy.props.CollectionProperty):
                return value[1]["type"]
    return None

def iter_my_deps_from_parent_id(cls, my_classes_by_idname):
    if bpy.types.Panel in cls.__bases__:
        parent_idname = getattr(cls, "bl_parent_id", None)
        if parent_idname is not None:
            parent_cls = my_classes_by_idname.get(parent_idname)
            if parent_cls is not None:
                yield parent_cls

def iter_my_classes(modules):
    base_types = get_register_base_types()
    for cls in get_classes_in_modules(modules):
        if any(base in base_types for base in cls.__bases__):
            if not getattr(cls, "is_registered", False):
                yield cls

def get_classes_in_modules(modules):
    classes = set()
    for module in modules:
        for cls in iter_classes_in_module(module):
            classes.add(cls)
    return classes

def iter_classes_in_module(module):
    for value in module.__dict__.values():
        if inspect.isclass(value):
            yield value

def get_register_base_types():
    return set(getattr(bpy.types, name) for name in [
        "UIList","Panel","PropertyGroup","AddonPreferences","Gizmo","GizmoGroup","Operator"
    ])


# Find order to register to solve dependencies
#################################################

def toposort(deps_dict):
    sorted_list = []
    sorted_values = set()
    while len(deps_dict) > 0:
        unsorted = []
        for value, deps in deps_dict.items():
            if len(deps) == 0:
                sorted_list.append(value)
                sorted_values.add(value)
            else:
                unsorted.append(value)
        deps_dict = {value : deps_dict[value] - sorted_values for value in unsorted}
    return sorted_list
