from bpy.types import AddonPreferences

from .base_ui import BaseUI, DrawExtension
from ..._auto_load import __main_package__


class Preferences(BaseUI, DrawExtension):
    bl_idname: str = __main_package__

    @classmethod
    def register(cls) -> AddonPreferences:
        return type(
            cls.__name__,
            (cls, AddonPreferences),
            {}
        )
