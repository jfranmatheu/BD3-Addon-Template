""" File generated automatically by addon_utils submodule. """
import bpy
from bpy.types import Context


class NiceGroup_Collection:
	def __getitem__(coll, index: int) -> 'NiceGroup': pass
	def add(coll) -> 'NiceGroup': pass
	def remove(coll, item_index: int) -> None: pass
	def clear(coll) -> None: pass

class TestTemporal:
	name: str
	test_string: str
	test_bool: bool

	@classmethod
	def get_data(cls: 'TestTemporal', context: Context) -> 'TestTemporal':
		return context.window_manager.test

class NiceGroup:
	name: str
	test_pointer_object: bpy.types.Object
	test_color: float

class TestScene:
	name: str
	test_bool: bool
	test_collection: NiceGroup_Collection

	@classmethod
	def get_data(cls: 'TestScene', context: Context) -> 'TestScene':
		return context.scene.test


# ++++++++++++++++++++++++++++++++++++++++++++++++++


class Data:
	TestTemporal = TestTemporal.get_data
	TestScene = TestScene.get_data

PG = Data # Alias.


# EXAMPLE ++++++++++++++++++++++++++++++++++++++++++++++++++
'''
from addon_template import types as addon_template_types

# Your property_group variable will have the correct typing. :-)
property_group = addon_template_types.TestTemporal.get_data(context)
property = property_group.test_string
print(property)
'''
