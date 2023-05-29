from bpy.props import *

from .property_enum import EnumPropertyHelper, DynamicEnumPropertyHelper
from .property_pointer import PointerPropertyTypes


class PropertyTypes:
    FLOAT = FloatProperty
    INT = IntProperty
    BOOL = BoolProperty
    FLOAT_VECTOR = FloatVectorProperty
    INT_VECTOR = IntVectorProperty
    BOOL_VECTOR = BoolVectorProperty
    ENUM_NATIVE = EnumProperty
    STRING = StringProperty
    POINTER_CUSTOM = PointerProperty

    IVECTOR_2 = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=2, **kwargs)
    IVECTOR_3 = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=3, **kwargs)
    IVECTOR_N = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=len(default_vector), **kwargs)
    VECTOR_2 = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=2, **kwargs)
    VECTOR_3 = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=3, **kwargs)
    VECTOR_N = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=len(default_vector), **kwargs)
    COLOR_RGB = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=3, **kwargs)
    COLOR_RGBA = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=4, **kwargs)
    DIRPATH = lambda **kwargs: StringProperty(subtype='DIR_PATH', **kwargs)
    FILEPATH = lambda **kwargs: StringProperty(subtype='FILE_PATH', **kwargs)

    POINTER = PointerPropertyTypes
    COLLECTION = lambda type, **kwargs: CollectionProperty(type=type, **kwargs)

    ENUM = EnumPropertyHelper
    ENUM_DYNAMIC = DynamicEnumPropertyHelper
