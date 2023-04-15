from .ops import OperatorTypes, OpsReturn, OpsModalFlags
from .preferences import AddonPreferences
from .ui import InterfaceTypes, PanelFlags
from .prop import PropertyGroup, Property


class BTypes:
    PREFS = AddonPreferences
    UI = InterfaceTypes
    OPS = OperatorTypes
    PROP_GROUP = PropertyGroup
    PROP = Property
