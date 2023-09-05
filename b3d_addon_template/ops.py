""" File generated automatically by addon_utils submodule. """
import bpy


def add_random_objects(*args, object_count: int = 1, use_random_rotation: bool = False) -> None:
	'''Add Random Objects. 

	Positional Arguments
	----------
	execution_context : ``set[str]``
		Determines the context that is given for the operator to run in, and whether invoke() is called or only execute()
		``EXEC_DEFAULT`` is used by default, running only the execute() method, but you may want the operator to take user interaction with ``INVOKE_DEFAULT`` which will also call invoke() if existing.

	undo : ``bool``
		Determines if the operator should push an undo.

	Keyword Arguments (Operator Properties)
	----------
	``object_count`` : ``int``, optional
		Number of objects to add randomly

	``use_random_rotation`` : ``bool``, optional
		Rotate the objects randomly

	Return
	----------
	Operators don’t have return values as you might expect, instead they return a set() which is made up of: {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}. Common return values are {'FINISHED'} and {'CANCELLED'}, the latter meaning that the operator execution was aborted without making any changes or saving an undo history entry.
	Calling an operator in the wrong context will raise a RuntimeError, there is a poll() method to avoid this problem.
	'''
	bpy.ops.b3d_addon_template.add_random_objects(*args, object_count=object_count, use_random_rotation=use_random_rotation)
