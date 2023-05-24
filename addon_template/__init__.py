import BAU


bl_info = BAU.AddonInfo(
    name = 'Addon Helper Module',
    description = 'Testing addon helper module',
    blender = (3, 5, 0),
    version = (0, 1, 0)
).bl_info

BAU.AutoLoad.magic()
