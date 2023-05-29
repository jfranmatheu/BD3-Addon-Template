from addon_template.ackit import Reg, EventType, EventValue

from .operator import NiceOperator


# [CTRL + E] shortcut will trigger [NiceOperator].
Reg.Helper.KEYMAP.OPERATOR(
    'Object Mode',
    NiceOperator,
    event_type='E',
    event_value=EventValue.PRESS,
    ctrl=True
)
