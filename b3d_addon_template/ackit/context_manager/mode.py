import bpy


class CM_ModeToggle:
  def __init__(self, context: bpy.types.Context, mode: str) -> None:
    self.prev_mode = context.mode
    if self.prev_mode == 'EDIT_MESH':
      self.prev_mode = 'EDIT'
    self.mode = mode
    self._skip = self.prev_mode == self.mode

  def __enter__(self):
    if self._skip: return
    bpy.ops.object.mode_set(False, mode=self.mode)
  
  def __exit__(self, exc_type, exc_value, trace):
    if self._skip: return
    bpy.ops.object.mode_set(False, mode=self.prev_mode)
