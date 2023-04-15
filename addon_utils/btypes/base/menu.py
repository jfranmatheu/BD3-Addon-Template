from .base_ui import BaseUI, UILayout
from ..._auto_load import __main_package__

from bpy.types import Menu as BlMenu


class Menu(BaseUI):
    @classmethod
    def draw_in_layout(cls, layout: UILayout, label: str = 'Menu'):
        layout.menu(cls.bl_idname, text=label)

    @classmethod
    def register(cls, deco_cls, label: str) -> BlMenu:
        return type(
            cls.__name__,
            (cls, BlMenu) if deco_cls is None else (cls, deco_cls, BlMenu),
            {
                'bl_idname': __main_package__ + '_MT_' + cls.__name__.lower(),
                'bl_label': label,
            }
        )
