from ctypes import Structure, c_bool, c_int, c_float, c_void_p, c_char, c_short


# bNodeType.type
class bNodeType_types:
    NODE_UNDEFINED = -2 # node type is not registered.
    NODE_CUSTOM = -1    # for dynamically registered custom types.
    NODE_GROUP = 2
    NODE_FRAME = 5
    NODE_REROUTE = 6
    NODE_GROUP_INPUT = 7
    NODE_GROUP_OUTPUT = 8
    NODE_CUSTOM_GROUP = 9


class CY_bNodeType(Structure):
    __fields__ = [
        ('idname', c_char * 64),
        ('type', c_int),
        
        ('ui_name', c_char * 64),
        ('ui_description', c_char * 256),
        ('ui_icon', c_int),
        
        ('width',  c_float), ('minwidth', c_float),  ('maxwidth',  c_float),
        ('height', c_float), ('minheight', c_float), ('maxheight', c_float),
        ('nclass', c_short),
        ('flag', c_short),
    ]
