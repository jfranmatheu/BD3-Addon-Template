from bpy.types import Context, UILayout

from addon_template.ackit import Reg

from .operator import NiceOperator


class NicePanel(Reg.Type.UI.MENU):
    label = 'Test Menu'

    def draw_ui(self, context: Context, layout: UILayout):
        layout.operator('render.render', text="Render Me!")
        NiceOperator.draw_in_layout(layout, label="Action!")
