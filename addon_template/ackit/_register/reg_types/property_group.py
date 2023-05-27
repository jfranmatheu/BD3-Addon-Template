from bpy import types as btypes

from typing import Type

from ._base import BTypeBase, GLOBALS


class PropertyGroup(BTypeBase):
    @classmethod
    def tag_register(deco_cls) -> Type['PropertyGroup']:
        return super().tag_register(btypes.PropertyGroup, 'PG')
