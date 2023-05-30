from bpy.types import Window, Scene, WorkSpace

from addon_template.ackit import Reg


prev_scene_pointer = 0
prev_workspace_pointer = 0


@Reg.RNA_LISTENER(Window, 'scene', persistent=True)
def on_scene_change(context, wnd: Window, scene: Scene):
    global prev_scene_pointer
    is_init = prev_scene_pointer == 0
    if is_init:
        print("Scene Initialization!")
    curr_scene_pointer = scene.as_pointer()
    if curr_scene_pointer == prev_scene_pointer:
        return
    prev_scene_pointer = curr_scene_pointer
    print("Scene changed! ->", scene.name)


@Reg.RNA_LISTENER(Window, 'workspace', persistent=True)
def on_workspace_change(context, wnd: Window, workspace: WorkSpace):
    global prev_workspace_pointer
    is_init = prev_workspace_pointer == 0
    if is_init:
        print("WorkSpace Initialization!")
    curr_workspace_pointer = workspace.as_pointer()
    if curr_workspace_pointer == prev_workspace_pointer:
        return
    prev_workspace_pointer = curr_workspace_pointer
    print("Workspace changed! ->", workspace.name)
