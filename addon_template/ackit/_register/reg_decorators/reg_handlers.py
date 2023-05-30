from enum import Enum, auto
from collections import defaultdict

import bpy
from bpy.app import handlers

# from .debug import print_debug


registered_handlers = defaultdict(list)

class Handlers(Enum):
    LOAD_PRE = auto()
    LOAD_POST = auto()
    ANNOTATION_PRE = auto()
    ANNOTATION_POST = auto()
    COMPOSITE_PRE = auto()
    COMPOSITE_POST = auto()
    COMPOSITE_CANCEL = auto()
    DEPSGRAPH_UPDATE_PRE = auto()
    DEPSGRAPH_UPDATE_POST = auto()
    FRAME_CHANGE_PRE = auto()
    FRAME_CHANGE_POST = auto()
    LOAD_FACTORY_PREFERENCES_PRE = auto()
    LOAD_FACTORY_PREFERENCES_POST = auto()
    OBJECT_BAKE_PRE = auto()
    OBJECT_BAKE_COMPLETE = auto()
    OBJECT_BAKE_CANCEL = auto()
    REDO_PRE = auto()
    REDO_POST = auto()
    RENDER_PRE = auto()
    RENDER_POST = auto()
    RENDER_INIT = auto()
    RENDER_COMPLETE = auto()
    RENDER_CANCEL = auto()
    RENDER_STATS = auto()
    RENDER_WRITE = auto()
    UNDO_PRE = auto()
    UNDO_POST = auto()
    VERSION_UPDATE = auto()
    XR_SESSION_START_PRE = auto()

    def __call__(self, persistent: bool = False):
        ''' Use as a decorator. Only 1 parameter is required in target function, which is context. '''
        return self.register(persistent=persistent)

    def register(self, persistent: bool = False):
        print(f"Registering... {self.name} Handler!")
        def decorator(deco_fun):

            def callback_deco(_deco_fun):
                def wrapper(*args, **kwargs):
                    print(f"{self.name} Handler was called!") # _deco_fun.handler_type
                    return _deco_fun(bpy.context)
                return wrapper

            deco_fun = callback_deco(deco_fun)
            if persistent:
                deco_fun = handlers.persistent(deco_fun)
            setattr(deco_fun, 'handler_type', self.name)
            getattr(handlers, self.name.lower()).append(deco_fun)
            registered_handlers[self.name].append(deco_fun)
            return deco_fun
        return decorator

    def unregister_all(self):
        if self.name not in registered_handlers:
            return
        handler_type = getattr(handlers, self.name.lower())
        for handler in registered_handlers[self.name]:
            if handler in handler_type:
                handler_type.remove(handler)
        del registered_handlers[self.name]


def unregister():
    for handler_type in Handlers:
        handler_type.unregister_all()
