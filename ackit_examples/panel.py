from bpy.types import Context, UILayout

from addon_template.ackit import Reg, SpaceType

from .operator import NiceOperator


@Reg.Flag.Panel.HIDE_HEADER # Optional Flag to hide the header of the panel.
class NicePanel(Reg.Type.UI.PANEL):
    space_type = SpaceType.VIEW_3D
    tab = 'Nice'
    # label = 'Nice Panel' # using HIDE_HEADER flag...

    def draw_ui(self, context: Context, layout: UILayout):
        layout.label(text="Hello World!", icon='MONKEY')
        NiceOperator.draw_in_layout(layout, label="Action!")


class NicePopoverPanel(Reg.Type.UI.POPOVER):
    space_type = SpaceType.VIEW_3D
    label = 'Popover Panel'

    def draw_ui(self, context: Context, layout: UILayout):
        layout.label(text="Popover Panel Content!")
        NiceOperator.draw_in_layout(layout, label="Action! :-)")
