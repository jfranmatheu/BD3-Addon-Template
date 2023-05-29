from addon_template.ackit import Reg, Property

from bpy.types import Scene, Object


Reg.Helper.PROP(Scene, 'my_property', Property.FILEPATH())

Reg.Helper.PROP_BATCH(Object,
    my_uuid=Property.STRING(),
    test_bool=Property.BOOL(),
    proxy_mesh=Property.POINTER.OBJECT('Proxy Mesh')
)
