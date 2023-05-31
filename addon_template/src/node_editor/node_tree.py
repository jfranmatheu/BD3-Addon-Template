from addon_template.ackit import Reg


class CoolNodeTree(Reg.Type.NodeEditor.NODE_TREE):
    label = "Cool Node Editor Tree"
    icon = 'MONKEY'
    idname = "AddonTemplate"

    def update(self) -> None:
        return super().update()
