from .ops import OperatorTypes, OpsReturn, OpsModalFlags
from .preferences import AddonPreferences
from .ui import InterfaceTypes, PanelFlags
from .property import PropertyTypes as Property
# from .prop import PropertyGroup, Property


class RegType:
    PREFS = AddonPreferences
    UI = InterfaceTypes
    OPS = OperatorTypes
    # PROP_GROUP = PropertyGroup
    # PROP = Property
