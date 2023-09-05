from bpy.types import AddonPreferences

from .ui._base_ui import BaseUI, DrawExtension
from ..._globals import GLOBALS


class ACK_AddonPreferences(BaseUI, DrawExtension):
    bl_idname: str = GLOBALS.ADDON_MODULE

    @classmethod
    def tag_register(cls) -> 'ACK_AddonPreferences':
        return super().tag_register(cls, AddonPreferences, None)
