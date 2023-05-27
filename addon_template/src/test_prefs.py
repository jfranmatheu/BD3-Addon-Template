from bpy.types import Context, UILayout

from addon_template.ackit import Reg


class TestPreferences(Reg.Type.PREFS):
    def draw_ui(self, context: Context, layout: UILayout):
        layout.label(text="Hello World! This is just some test :-)")
