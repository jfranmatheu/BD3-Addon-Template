import bpy

from addon_template.ackit import Reg


@Reg.HANDLER.LOAD_POST(persistent=True)
def on_load_post(context):
    print("on load post callback!!!!!!!!! :-D")
