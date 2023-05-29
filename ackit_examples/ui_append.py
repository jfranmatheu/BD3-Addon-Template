from addon_template.ackit import Reg

from bl_ui.space_view3d import VIEW3D_HT_header


@Reg.Deco.UI_APPEND(VIEW3D_HT_header, poll=lambda header, ctx: ctx.mode == 'OBJECT', prepend=False)
def view3d_header_append(header, context):
    header.layout.label(text="HELLO WORLD!!!!!!!", icon='MONKEY')
