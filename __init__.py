bl_info = {
    "name" : "Test Addon",
    "author" : "J. Fran Matheu (@jfranmatheu)",
    "description" : "",
    "blender" : (3, 5, 0),
    "version" : (0, 1, 0),
    "location" : "",
    "warning" : "This is just a test",
    "category" : "General",
}

from .addon_utils import AutoLoad

AutoLoad.initialize()
