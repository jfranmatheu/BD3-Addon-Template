from string import Template



coll_class_wrapper_template = Template("""
class ${class_name}_Collection:
\tdef __getitem__(coll, index: int) -> '${class_name}': pass
\tdef add(coll) -> '${class_name}': pass
\tdef remove(coll, item_index: int) -> None: pass
\tdef clear(coll) -> None: pass
""")

pg_class_wrapper_template = Template("""
class ${class_name}:
${property_defs}
""")

pg_class_get_data_template = Template("""
\t@classmethod
\tdef get_data(cls: '${class_name}', context: Context) -> '${class_name}':
\t\treturn context.${pg_data_path}
""")

example_typing_template = Template("""
\n\n# EXAMPLE ++++++++++++++++++++++++++++++++++++++++++++++++++\n'''
from ${addon_module_name} import types as ${addon_module_name}_types

# Your property_group variable will have the correct typing. :-)
property_group = ${addon_module_name}_types.${pg_name}.get_data(context)
property = property_group.${prop_name}
print(property)
'''\n""")


def prop_type_to_py_type(prop) -> str:
    # print(dir(prop))
    bpy_prop_name = type(prop).__name__
    is_vector = 'Vector' in bpy_prop_name
    if 'Float' in bpy_prop_name:
        return 'tuple[float]' if is_vector else 'float'
    if 'Int' in bpy_prop_name:
        return 'tuple[int]' if is_vector else 'int'
    if 'Bool' in bpy_prop_name:
        return 'tuple[bool]' if is_vector else 'bool'
    if 'String' in bpy_prop_name:
        return 'str'
    if 'Pointer' in bpy_prop_name:
        # print(prop.type, prop.fixed_type.name)
        return 'bpy.types.' + prop.fixed_type.name
    if 'Collection' in bpy_prop_name:
        #print(prop, prop.fixed_type, dir(prop.fixed_type), prop.fixed_type.original_idname)
        return f'{prop.fixed_type.original_idname}_Collection' # f'list[{prop.fixed_type.original_idname}]'
    return 'None'


def codegen__types_py(types_filepath: str | None = None) -> None:
    """Generates the Typing for PropertyGroup types.

    Args:
        types_filepath (str): path relative to the addon source where to write your types.py file. Defaults to '/types.py' (source root).
    """
    # Get PropertyGroup classes in the proper order.
    from .._register._register import BlenderTypes
    pg_classes = BlenderTypes.PropertyGroup.get_classes()
    if pg_classes == []:
        # SAD. No PropertyGroup classes to process... :-(
        return

    from .._auto_load import get_ordered_pg_classes_to_register
    pg_sorted_classes = get_ordered_pg_classes_to_register(pg_classes)


    # Search for PropertyGroup used as CollectionProperty inside other PropertyGroup class.
    classes_used_as_collection = []
    for pg in pg_sorted_classes:
        for prop_idname, prop in pg.bl_rna.properties.items():
            if prop_idname in {'rna_type', 'name'}:
                continue
            if 'Collection' not in type(prop).__name__:
                continue
            classes_used_as_collection.append(prop.fixed_type.original_idname)


    # WRITE TO FILE. ---------------------------
    from .._globals import GLOBALS
    if types_filepath is None:
        types_filepath = GLOBALS.CodeGen.TYPES
    output_path = GLOBALS.ADDON_SOURCE_PATH / types_filepath
    addon_module_name = GLOBALS.ADDON_MODULE

    with output_path.open('w') as f:
        f.write('""" File generated automatically by addon_utils submodule. """')
        f.write('\nimport bpy\nfrom bpy.types import Context\n\n')#from {addon_module_name}.addon_utils.prop import PGType\n\n')

        # Write the CollectionProperty classes we found with a nice template.
        for coll_cls_name in classes_used_as_collection:
            f.write(
                coll_class_wrapper_template.substitute(
                    class_name=coll_cls_name,
                )
            )

        # Just to store some PropertyGroup to use for the example code.
        example_pg_prop = None

        # For the Data Enumerator utility.
        root_pg_classes = []

        # Write to file the property groups.
        for pg in pg_sorted_classes:
            # print(pg, pg.bl_rna.properties)
            # is_root = pg.is_root
            is_root: bool = hasattr(pg, 'is_root') and pg.is_root
            f.write(
                pg_class_wrapper_template.substitute(
                    class_name=pg.original_idname,
                    property_defs='\n'.join([
                        f'\t{prop_idname}: {prop_type_to_py_type(prop)}'
                            for prop_idname, prop in pg.bl_rna.properties.items() # pg.__annotations__.items()
                            if prop_idname not in {'rna_type'}
                            #if isinstance(prop, _PropertyDeferred) and prop_idname not in {'rna_type'}
                    ]),

                )
            )

            # If it's a root PropertyGroup, we need to add a get_path() class method
            # to it to get the corresponding data with typing!.
            if is_root:
                f.write(
                    pg_class_get_data_template.substitute(
                        class_name=pg.original_idname,
                        pg_data_path=pg.data_path,
                    )
                )
                if example_pg_prop is None:
                    for prop_idname in pg.bl_rna.properties.keys():
                        if prop_idname not in {'rna_type', 'name'}:
                            example_pg_prop = (pg, prop_idname)
                            break

                root_pg_classes.append(pg.original_idname)

        # Write the Data enumerator.
        f.write("\n\n# ++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
        f.write('\nclass Data:')
        for root_pg_cls_name in root_pg_classes:
            f.write(f'\n\t{root_pg_cls_name} = {root_pg_cls_name}.get_data')
        
        f.write('\n\nPG = Data # Alias.')

        # Write example code.
        if example_pg_prop is not None:
            pg, prop_idname = example_pg_prop
            f.write(
                example_typing_template.substitute(
                    addon_module_name=addon_module_name,
                    pg_name=pg.original_idname,
                    prop_name=prop_idname
                )
            )
