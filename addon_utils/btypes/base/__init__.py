from .preferences import BasePreferences
from .operator import BaseOperator, OpsReturn
from .panel import BasePanel
from .menu import BaseMenu


class BaseBTypes:
    PREFERENCES = BasePreferences
    OPERATOR = BaseOperator
    PANEL = BasePanel
    MENU = BaseMenu
