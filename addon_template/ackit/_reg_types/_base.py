import bpy

from ._register import BlenderTypes
from .._globals import GLOBALS

from collections import defaultdict


class BTypeBase(object):
    @classmethod
    def __subclasses_recursive__(cls):
        direct = cls.__subclasses__()
        indirect = []
        for subclass in direct:
            indirect.extend(subclass.__subclasses_recursive__())
        return direct + indirect

    @classmethod
    def tag_register(cls, bpy_type: type or str, cls_name: str = None, *subtypes, **kwargs):
        if isinstance(bpy_type, str):
            bpy_type = getattr(bpy.types, bpy_type)
        print(f"[{GLOBALS.ADDON_MODULE}] Registering class '{cls.__name__}' of type '{bpy_type.__name__}'")
        new_cls = type(
            cls_name if cls_name is not None else cls.__name__,
            (cls, *subtypes, bpy_type),
            kwargs
        )
        getattr(BlenderTypes, bpy_type.__name__).add_class(new_cls)
        return new_cls



def init():
    for subcls in BTypeBase.__subclasses_recursive__():
        if 'addon_utils' in subcls.__module__ or 'types' in subcls.__module__:
            # SKIP: IF THE SUBCLASS IS INSIDE THE addon_utils module or inside any folder called 'types'.
            continue
        subcls.tag_register()
