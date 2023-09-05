import bpy
from bpy import types as bpy_types

from .._base import ACKType
from ...._globals import GLOBALS


DEFAULT_NODETREE_IDENTIFIER = f'{GLOBALS.ADDON_MODULE.upper()}_NodeTree'


class ACK_Node(ACKType):
    label: str = 'Custom Node'
    icon: str = 'NONE'
    category: str = 'Unasigned'

    node_tree_idname: str = DEFAULT_NODETREE_IDENTIFIER


    ###################################

    @classmethod
    def tag_register(deco_cls) -> 'ACK_Node':
        node_idname = f'{GLOBALS.ADDON_MODULE.upper()}_Node_{deco_cls.__name__}'

        node_tree = super().tag_register(
            bpy_types.Node, None,
            bl_idname=node_idname,
            bl_label=deco_cls.label,
            bl_icon=deco_cls.icon,
        )

        return node_tree
