from ..ackit import BTypes, bpy_t


class TestPreferences(BTypes.PREFS):
    def draw_ui(self, context: bpy_t.Context, layout: bpy_t.UILayout):
        layout.label(text="Hello World! This is just some test :-)")
