import bpy
from bpy.types import Operator, OperatorProperties, UILayout, Context, Event

import re

from ..._auto_load import __main_package__


class OpsReturn:
    FINISH = {'FINISHED'}
    CANCEL = {'CANCELLED'}
    PASS = {'PASS_THROUGH'}
    RUN = {'RUNNING_MODAL'}
    UI = {'INTERFACE'}


class Operator:
    ''' Base Class for Operator types.
        Class Properties:
            - 'label': aka bl_label.
        Class Methods:
            - 'create_operator': creates an Operator type class.
            - 'run': to run this operator. (classmethod)
            - 'run_invoke': to run this operator but with invoke execution context. (classmethod)
            - 'draw_in_layout': to draw a button in the UI for this operator. (classmethod)
            - 'invoke': the Operator.invoke method, it calls execute by default.
            - 'execute': the Operator.execute method, it calls the action method by default.
            - 'action': a fast way to perform any action you need, does not requires to return OpsReturn manually.
    '''
    bl_idname: str

    label: str

    @classmethod
    def poll(cls, context: Context) -> bool:
        return True

    def invoke(self, context: Context, event: Event) -> OpsReturn:
        # print("BaseOperator::invoke() -> ", self.bl_idname)
        return self.execute(context)

    def action(self, context: 'Context') -> None:
        # print("BaseOperator::action() -> ", self.bl_idname)
        pass

    def execute(self, context: 'Context') -> OpsReturn:
        # print("BaseOperator::execute() -> ", self.bl_idname)
        self.action(context)
        return OpsReturn.FINISH


    ###################################
    
    @classmethod
    def register(cls):
        keywords = re.findall('[A-Z][^A-Z]*', cls.__name__)
        idname: str = '_'.join([word.lower() for word in keywords])

        return type(
            __main_package__.upper() + '_OT_' + idname,
            (cls, Operator),
            {
                'bl_label': cls.label if hasattr(cls, 'label') else ' '.join(keywords),
                'bl_idname': __main_package__.lower() + '.' + idname,
            }
        )

    @classmethod
    def run(cls, **operator_properties: dict) -> None:
        eval('bpy.ops.'+cls.bl_idname)(**operator_properties)

    @classmethod
    def run_invoke(cls, **operator_properties: dict) -> None:
        eval('bpy.ops.'+cls.bl_idname)('INVOKE_DEFAULT', **operator_properties)

    @classmethod
    def draw_in_layout(cls,
                       layout: UILayout,
                       label: str = None,
                       op_props: dict = {},
                       **draw_kwargs: dict) -> OperatorProperties:
        op = layout.operator(cls.bl_idname, text=label if label is not None else cls.label, **draw_kwargs)
        if op_props:
            for key, value in op_props.items():
                setattr(op, key, value)
        return op
