
import bpy
import math
import textwrap
from . import addon_updater_ops
from . import xie_ops
                             
from mathutils import (Matrix,
                        Vector,
                        )
                       
from bpy.types import (Operator,
                        )


class OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation(Operator):
    """FFXIV IK Export - Bake IK Animation"""
    bl_idname = "object.ffxiv_ik_export_bake_ik_animation"
    bl_label = "Bake IK Animation to FFXIV Skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        xie_tool = scene.xie_tool
        ik_action = xie_tool.ik_rig.animation_data.action

        for ob in bpy.context.selected_objects:
            ob.select_set(False)

        xie_tool.fk_rig.select_set(True)

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.duplicate()

        dupli_obj = bpy.context.object
        dupli_obj.name = ik_action.name.replace("IK", "FFXIV Anim")

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.nla.bake(frame_start=scene.frame_start, frame_end=scene.frame_end, only_selected=False, visual_keying=True, clear_constraints=True, use_current_action=False, bake_types={'POSE'})
        dupli_obj.animation_data.action.name = ik_action.name.replace("IK", "FFXIV")
        
        return {'FINISHED'}

classes = (
    OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation,
)

def register():    
    from bpy.utils import register_class
    for cls in classes:
        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)