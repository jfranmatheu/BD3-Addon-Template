


class Register:
    PREFS = AddonPreferencesRegister






#####################################################
# Diferent Method for addon_utils class management. #
#####################################################
'''
from bpy.types import Operator

class BaseClass:
    label: str
    
    def print_cat(self):
        print("Cat")

def register(decorated_cls) -> BaseClass:
    new_cls = type(
        decorated_cls.__name__,
        (decorated_cls, BaseClass, Operator),
        {}
    )
    return new_cls

@register
class Test:
    # 1. You type 'label' or 'print_cat' here and the IDE knows anything about BaseClass
    
    def print_dog(self):
        print("Dog")

# 2. But here, Test knows that 'print_cat' is something.
Test.print_cat
'''
########################################
'''
from bpy.types import Operator


class BaseClass:
    label: str

    def print_cat(self):
        print("Cat")

    @classmethod
    def register(cls, decorated_cls, label: str = '') -> 'BaseClass':
        new_cls = type(
            decorated_cls.__name__,
            (decorated_cls, Operator),
            {
                'label': label,
            }
        )
        return new_cls

@BaseClass.register(label='HELLO')
class Test(BaseClass):
    def print_dog(self):
        print("Dog")
'''
########################################
'''
from bpy.types import Operator


class BaseClass(Operator):
    label: str

    def print_cat(self):
        print("Cat")

class Test(BaseClass):
    def print_dog(self):
        print("Dog")

from bpy.utils import register_classes_factory

register, unregister = register_classes_factory(BaseClass.__subclasses__())
'''
########################################