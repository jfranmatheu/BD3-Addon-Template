from ._base_ui import BaseUI, UILayout
from ...globals import GLOBALS

from bpy.types import Menu as BlMenu


class Menu(BaseUI):
    @classmethod
    def draw_in_layout(cls, layout: UILayout, label: str = None):
        layout.menu(cls.bl_idname, text=label if label else cls.bl_label)

    @classmethod
    def tag_register(deco_cls) -> 'Menu':
        return super().tag_register(
            BlMenu,
            bl_idname=GLOBALS.ADDON_MODULE + '_MT_' + deco_cls.__name__.lower(),
            bl_label=deco_cls.label if hasattr(deco_cls, 'label') else deco_cls.__name__)
