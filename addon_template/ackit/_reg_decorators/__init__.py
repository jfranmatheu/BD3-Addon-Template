from .reg_operator import OperatorRegister
from .reg_ui import UIRegister
from .reg_property import PropertyRegister, BatchPropertyRegister
from .reg_property_group import PropertyGroupRegister
from .reg_shortcut import ShortcutRegister
from .reg_prefs import AddonPreferencesRegister
from .reg_tool import ToolsRegister

from .reg_rna_sub import subscribe_to_rna_change # RNASubscription
from .reg_timer import new_timer_as_decorator


class RegDeco:
    PREFS = AddonPreferencesRegister
    OPS = OperatorRegister
    UI = UIRegister
    PROP_GROUP = PropertyGroupRegister
    PROP = PropertyRegister
    PROP_BATCH = BatchPropertyRegister
    SHORTCUT = ShortcutRegister
    TOOLS = ToolsRegister
    RNA_SUB = subscribe_to_rna_change
    TIMER = new_timer_as_decorator
