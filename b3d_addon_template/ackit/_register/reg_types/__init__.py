from .ops import OperatorTypes, OpsReturn, ACK_ModalFlags
from .preferences import ACK_AddonPreferences
from .ui import InterfaceTypes, ACK_PanelFlags
from .property_group import ACK_PropertyGroup
from .node_editor import NodeEditorTypes
from .property_types import PropertyTypes


class RegType:
    PREFS = ACK_AddonPreferences
    UI = InterfaceTypes
    OPS = OperatorTypes
    PROP_GROUP = ACK_PropertyGroup
    NODE_EDITOR = NodeEditorTypes
    PROPS = PropertyTypes

    class Flag:
        Modal = ACK_ModalFlags # Decorator.
        Panel = ACK_PanelFlags # Decorator.
