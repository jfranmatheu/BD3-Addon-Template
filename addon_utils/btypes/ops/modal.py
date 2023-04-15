from enum import Enum, auto

from bpy import types as bpy_types

from ...types.event import EventType, EventValue, Mouse
from .operator import Operator, OpsReturn


class OpsModalFlags(Enum):
    class Raycast(Enum):
        BVHTREE = auto()
        SCENE = auto()
        OBJECT = auto()

    DRAW_2D = auto()
    DRAW_3D = auto()


class ModalOperator(Operator):
    # Properties you should set in your subclasses.
    modal_flags: set[OpsModalFlags]

    # --------------------------------

    mouse: Mouse

    def invoke(self, context: bpy_types.Context, event: bpy_types.Event) -> OpsReturn:
        # print("BaseOperator::invoke() -> ", self.bl_idname)
        if not context.window_manager.modal_handler_add(self):
            return OpsReturn.CANCEL
        self.mouse = Mouse.init(event)
        return OpsReturn.RUN

    def modal(self, context: bpy_types.Context, event: bpy_types.Event) -> OpsReturn:
        if event.type in {EventType.MOUSEMOVE, EventType.INBETWEEN_MOUSEMOVE}:
            self.mouse.update(event)
            self.mouse_move(context, self.mouse)
            return OpsReturn.RUN
        return self.modal_update(context, event)

    def mouse_move(self, context: bpy_types.Context, mouse: Mouse) -> None:
        pass

    def modal_update(self, context: bpy_types.Context, event: bpy_types.Event) -> OpsReturn:
        return OpsReturn.RUN

    def execute(self, context: bpy_types.Context) -> OpsReturn:
        return OpsReturn.CANCEL

    #############################

    @classmethod
    def tag_register(deco_cls, flags: set[OpsModalFlags] = set()) -> 'ModalOperator':
        return super().tag_register()
