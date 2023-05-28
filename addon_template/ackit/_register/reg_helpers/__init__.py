from .help_shortcut import ShortcutRegister
from .help_property import PropertyRegister, BatchPropertyRegister


class RegHelper:
    KEYMAP = ShortcutRegister
    MACRO = None # TODO: Code the helper.
    PROP = PropertyRegister
    PROP_BATCH = BatchPropertyRegister
