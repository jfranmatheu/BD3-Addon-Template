from dataclasses import dataclass
from typing import Type, Any
from string import Template

from bpy.types import (
    bpy_struct,
    Property,
    FloatProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
    EnumProperty
)


docstring_parameter_template = Template(
"""\t``${idname}`` : ``${type}``${optional}
\t\t${description}""")

operator_call_docstring_template = Template("""
\t'''${bl_label}. ${bl_description}\n
\tPositional Arguments
\t----------
\texecution_context : ``set[str]``
\t\tDetermines the context that is given for the operator to run in, and whether invoke() is called or only execute()
\t\t``EXEC_DEFAULT`` is used by default, running only the execute() method, but you may want the operator to take user interaction with ``INVOKE_DEFAULT`` which will also call invoke() if existing.

\tundo : ``bool``
\t\tDetermines if the operator should push an undo.

\tKeyword Arguments (Operator Properties)
\t----------
${parameters}

\tReturn
\t----------
\tOperators don’t have return values as you might expect, instead they return a set() which is made up of: {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}. Common return values are {'FINISHED'} and {'CANCELLED'}, the latter meaning that the operator execution was aborted without making any changes or saving an undo history entry.
\tCalling an operator in the wrong context will raise a RuntimeError, there is a poll() method to avoid this problem.
\t'''""")

operator_call_template = Template("""
def ${ori_cls_name}(*args${kwargs}) -> None:${docstring}
\tbpy.ops.${op_idname}(*args${kwargs_pass})
\n""")


@dataclass
class WriteProperty:
    idname: str
    type: Type[Any]
    default: Any


def get_type_value(property: Property) -> tuple[str, Any]:
    if isinstance(property, IntProperty):
        return (int, property.default_array) if property.array_length > 1 else (int, property.default)
    if isinstance(property, FloatProperty):
        return (float, property.default_array) if property.array_length > 1 else (float, property.default)
    if isinstance(property, StringProperty):
        return (str, property.default)
    if isinstance(property, BoolProperty):
        return (bool, property.default)
    if isinstance(property, EnumProperty):
        return (str, property.default)
    return '', ''


def codegen__ops_py(ops_filepath = None):
    from .._register.reg_types._base import BlenderTypes
    from .. import ack_types
    from .._globals import GLOBALS

    if ops_filepath is None:
        ops_filepath = GLOBALS.CodeGen.OPS
    output_path = GLOBALS.ADDON_SOURCE_PATH / ops_filepath

    with output_path.open('w+') as f:
        f.write('""" File generated automatically by addon_utils submodule. """')
        f.write('\nimport bpy\n\n')

        ack_ops_classes: list[Type[ack_types.OPS.ACTION]] = BlenderTypes.Operator.get_classes()

        for ack_op_cls in ack_ops_classes:
            op = ack_op_cls.get_operator()
            op_rna: bpy_struct = op.get_rna_type()
            op_props: dict[str, Property] = op_rna.properties

            kwargs = ''
            kwargs_pass = ''
            docstring_parameters = ''
            tot_props = len(op_props)
            # print("tot props: ", tot_props)
            for prop_name, prop in op_props.items():
                tot_props -= 1
                if prop_name in {'rna_type'}:
                    continue

                prop_type, prop_value = get_type_value(prop)
                if isinstance(prop_value, str):
                    kwargs += f', {prop_name}: {prop_type.__name__} = "{prop_value}"'
                else:
                    kwargs += f', {prop_name}: {prop_type.__name__} = {prop_value}'
                kwargs_pass += f', {prop_name}={prop_name}'

                docstring_parameters += docstring_parameter_template.substitute(
                    idname=prop_name,
                    type=prop_type.__name__,
                    optional=', optional' if (not isinstance(prop_value, str) or (isinstance(prop_value, str) and prop_value == '')) else '',
                    description=prop.description if prop.description != '' else prop.name,
                )

                if tot_props == 0:
                    break

                docstring_parameters += '\n\n'
            
            if docstring_parameters == '':
                docstring_parameters = '\tNo operator propertiest to pass.'

            bl_idname = ack_op_cls.bl_idname

            docstring = operator_call_docstring_template.substitute(
                bl_label=ack_op_cls.bl_label,
                bl_description=ack_op_cls.bl_description,
                parameters=docstring_parameters
            )

            f.write(operator_call_template.substitute(
                ori_cls_name=bl_idname.split('.')[1], # ack_op_cls.ori_cls.__name__,
                op_idname=bl_idname,
                kwargs=kwargs,
                kwargs_pass=kwargs_pass,
                docstring=docstring
            ))
