from ..addon_utils import BTypes, bpy_t


class TestOp(BTypes.OPS.ACTION):
    def action(self, context: bpy_t.Context) -> None:
        print("Hello World! This a test operator :-D")
