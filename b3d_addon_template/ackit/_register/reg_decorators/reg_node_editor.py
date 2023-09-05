from typing import Tuple

from ..reg_types.node_editor.node_tree import ACK_NodeTree
from ..reg_types.node_editor.node import ACK_Node

from ..._globals import GLOBALS


DEFAULT_NODETREE_IDENTIFIER = f'{GLOBALS.ADDON_MODULE.upper()}_NodeTree'


def register_node_editor(name: str, icon: str, identifier: str = DEFAULT_NODETREE_IDENTIFIER) -> ACK_NodeTree:
    ''' Returns the NodeTree class which gives you access to the Node base class. '''
    pass
