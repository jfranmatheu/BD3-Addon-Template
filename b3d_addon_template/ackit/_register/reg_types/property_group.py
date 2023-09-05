from bpy import types as bpy_types

from typing import Type

from ._base import ACKType, GLOBALS


class ACK_PropertyGroup(ACKType):
    ''' For CHILD PropertyGroup ONLY.
        DON'T USE for ROOT PropertyGroup (instead use Reg.Deco.PROP_GROUP.ROOT.).'''

    @classmethod
    def tag_register(cls) -> Type['ACK_PropertyGroup']:
        return super().tag_register(bpy_types.PropertyGroup, 'PG', is_root=False)
