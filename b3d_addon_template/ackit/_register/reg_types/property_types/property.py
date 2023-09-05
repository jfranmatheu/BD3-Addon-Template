from bpy.props import *
from mathutils import Matrix

from .property_enum import EnumPropertyHelper, DynamicEnumPropertyHelper
from .property_pointer import PointerPropertyTypes
from .property_collection import CollectionPropertyHelper


class PropertyTypes:
    FLOAT = FloatProperty
    INT = IntProperty
    BOOL = BoolProperty
    FLOAT_VECTOR = FloatVectorProperty
    INT_VECTOR = IntVectorProperty
    BOOL_VECTOR = BoolVectorProperty
    ENUM = EnumProperty
    STRING = StringProperty
    POINTER = PointerProperty
    COLLECTION = lambda type, **kwargs: CollectionProperty(type=type, **kwargs)

    FACTOR = lambda default_value, **kwargs: FloatProperty(default=default_value, min=0.0, max=1.0)

    VECTOR_INT_2 = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=2, **kwargs)
    VECTOR_INT_3 = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=3, **kwargs)
    VECTOR_INT_N = lambda default_vector, **kwargs: IntVectorProperty(default=default_vector, size=len(default_vector), **kwargs)
    VECTOR_2 = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=2, **kwargs)
    VECTOR_3 = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=3, **kwargs)
    VECTOR_N = lambda default_vector, **kwargs: FloatVectorProperty(default=default_vector, size=len(default_vector), **kwargs)
    COLOR_RGB = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=3, subtype='COLOR', **kwargs)
    COLOR_RGBA = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=4, subtype='COLOR', **kwargs)
    COLOR_GAMMA_RGB = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=3, subtype='COLOR_GAMMA', **kwargs)
    COLOR_GAMMA_RGBA = lambda name, default_color, **kwargs: FloatVectorProperty(name=name, default=default_color, min=0.0, max=1.0, size=4, subtype='COLOR_GAMMA', **kwargs)
    XYZ = lambda default_vector, **kwargs: PropertyTypes.VECTOR_3(default_vector, subtype='XYZ', **kwargs)
    ANGLE_AXIS = lambda **kwargs: PropertyTypes.VECTOR_3((0, 0, 0), subtype='AXISANGLE', **kwargs)
    ANGLE_EULER = lambda **kwargs: PropertyTypes.VECTOR_3((0, 0, 0), subtype='EULER', **kwargs)
    ANGLE_QUATERNION = lambda **kwargs: PropertyTypes.VECTOR_N((0, 0, 0, 0), subtype='QUATERNION', **kwargs)
    MATRIX_2x2 = lambda **kwargs: PropertyTypes.VECTOR_N(Matrix.Identity(size=2), subtype='MATRIX', **kwargs)
    MATRIX_3x3 = lambda **kwargs: PropertyTypes.VECTOR_N(Matrix.Identity(size=3), subtype='MATRIX', **kwargs)
    MATRIX_4x4 = lambda **kwargs: PropertyTypes.VECTOR_N(Matrix.Identity(size=4), subtype='MATRIX', **kwargs)

    DIRPATH = lambda **kwargs: StringProperty(subtype='DIR_PATH', **kwargs)
    FILEPATH = lambda **kwargs: StringProperty(subtype='FILE_PATH', **kwargs)

    POINTER__HELPER = PointerPropertyTypes
    # COLLECTION__HELPER = CollectionPropertyHelper # Not implemented yet. Should create an empty collection with a pointer of the selected type.

    ENUM__HELPER = EnumPropertyHelper
    ENUM_DYN__HELPER = DynamicEnumPropertyHelper
