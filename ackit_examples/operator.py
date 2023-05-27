from bpy.types import Context

from addon_template.ackit import Reg


class NiceOperator(Reg.Type.OPS.ACTION):
    def action(self, context: Context) -> None:
        print("Action!", context.object.name)
