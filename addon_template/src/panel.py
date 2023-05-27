from bpy.types import Context, UILayout

from addon_template.ackit import Reg, SpaceType

from .operator import NiceOperator


@Reg.Flag.Panel.HIDE_HEADER
class NicePanel(Reg.Type.UI.PANEL):
    space_type = SpaceType.VIEW_3D
    tab = 'Nice'
    # label = 'Nice Panel' # using HIDE_HEADER flag...

    def draw_ui(self, context: Context, layout: UILayout):
        layout.label(text="Hello World!", icon='MONKEY')
        NiceOperator.draw_in_layout(layout, label="Action!")
