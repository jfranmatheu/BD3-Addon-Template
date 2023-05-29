from .types import codegen__types_py
from .ops import codegen__ops_py
from .icons import codegen__icons_py


# TODO: a predefinied file with all global variables... editable by other devs easily.
# Then, load that data and use it for the paths of auto generated code...


class AddonCodeGen:
    TYPES = codegen__types_py # Typing for PropertyGroup types.
    ICONS = codegen__icons_py # Quick access to project icons. (to use in enums, UI items, shaders, etc.)
    OPS   = codegen__ops_py   # Typing for Operator types. Useful to find and call them from this.
