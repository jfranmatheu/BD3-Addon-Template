from .ackit import AddonInfo


bl_info = AddonInfo()

from .ackit import AutoLoad
AutoLoad.magic(works_in_background=False)
