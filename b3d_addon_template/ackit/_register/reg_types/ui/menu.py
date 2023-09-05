from ._base_ui import BaseUI, UILayout
from ...._globals import GLOBALS

from bpy.types import Menu as BlMenu


ui_idname_cache = {}


class ACK_Menu(BaseUI):
    label: str

    @classmethod
    def draw_in_layout(cls, layout: UILayout, label: str = None):
        layout.menu(cls.bl_idname, text=label if label else cls.bl_label)

    @classmethod
    def tag_register(deco_cls) -> 'ACK_Menu':
        return super().tag_register(BlMenu, 'MT')
