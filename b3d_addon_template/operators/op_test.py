from b3d_addon_template.ackit import ack_types, bpy_types, PropertyTypes

import bpy

from random import random


class AddRandomObjects(ack_types.OPS.ACTION):
    label = 'Add Random Objects'

    object_count: PropertyTypes.INT(name="Object Count", description="Number of objects to add randomly", min=1, default=1)
    use_random_rotation: PropertyTypes.BOOL(name="Random Rotation", description="Rotate the objects randomly")

    def action(self, context: bpy_types.Context) -> None:
        for i in range(self.object_count):
            rotation = (random()*360, random()*360, random()*360) if self.use_random_rotation else (0, 0, 0)
            bpy.ops.object.empty_add(rotation=rotation)
