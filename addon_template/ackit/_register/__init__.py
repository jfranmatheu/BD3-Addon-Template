# INTERNAL SUBMODULE
# MODIFY IT ONLY IF YOU KNOW WHAT YOU ARE DOING

from .reg_decorators import RegDeco
from .reg_types import RegType, OpsReturn, ModalFlags, PanelFlags
from .reg_helpers import RegHelper

class Reg:
    Deco = RegDeco
    Helper = RegHelper
    Type = RegType

    class Flag:
        Modal = ModalFlags # Decorator.
        Panel = PanelFlags # Decorator.


def clear_register_cache():
    from ._register import clear_cache
    clear_cache()
    # from .reg_types._base import BTypeBase
    # BTypeBase.clear_cache()
