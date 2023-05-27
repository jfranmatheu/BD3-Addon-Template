#bl_info = ackit.AddonInfo(
#    name = 'Addon based on ackit',
#    description = 'Testing ackit helper module',
#    blender = (3, 5, 1),
#    version = (0, 1, 0)
#)

bl_info = {
    'name': 'Addon based on ackit',
    'author': 'JF',
    'description': 'Testing ackit helper module',
    'blender': (3, 5, 1),
    'version': (0, 1, 0),
    'location': 'Anywhere'
}

from . import ackit
ackit.AutoLoad.magic(works_in_background=False)
