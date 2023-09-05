# INTERNAL SUBMODULE
# MODIFY IT ONLY IF YOU KNOW WHAT YOU ARE DOING

from .reg_decorators import RegDeco
from .reg_types import RegType, OpsReturn, ACK_ModalFlags, ACK_PanelFlags, PropertyTypes
from .reg_helpers import RegHelper


class Reg:
    Deco = RegDeco
    Helper = RegHelper
    Type = RegType

    class Flag:
        Modal = ACK_ModalFlags # Decorator.
        Panel = ACK_PanelFlags # Decorator.
