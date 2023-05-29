from addon_template.ackit import Reg, Property


@Reg.Deco.PROP_GROUP.CHILD
class NiceGroup:
    test_pointer_object: Property.POINTER.OBJECT('Test Object')
    test_color: Property.COLOR_RGBA('Test Color', (1, .6, .4, 1.0))


@Reg.Deco.PROP_GROUP.ROOT.SCENE('test')
class TestScene:
    test_bool: Property.BOOL()
    test_collection: Property.COLLECTION(NiceGroup)


@Reg.Deco.PROP_GROUP.ROOT.WINDOW_MANAGER('test')
class TestTemporal:
    test_string: Property.STRING()
    test_bool: Property.BOOL()
