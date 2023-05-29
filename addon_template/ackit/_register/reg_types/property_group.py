from bpy import types as btypes

from typing import Type

from ._base import BTypeBase, GLOBALS


class PropertyGroup(BTypeBase):
    ''' For CHILD PropertyGroup ONLY.
        DON'T USE for ROOT PropertyGroup (instead use Reg.Deco.PROP_GROUP.ROOT.).'''

    @classmethod
    def tag_register(deco_cls) -> Type['PropertyGroup']:
        return super().tag_register(btypes.PropertyGroup, 'PG', is_root=False)
