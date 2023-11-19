
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
    bl_label = "Bakes IK Animation to a duplicate of the FFXIV Skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        xie_tool = scene.xie_tool

        ik_rig = xie_tool.ik_rig
        fk_rig = xie_tool.fk_rig

        bpy.ops.object.mode_set(mode='EDIT')
        bone_to_duplicate = fk_rig.data.edit_bones['n_root']
        arm.data.edit_bones.active = bone_to_duplicate
        arm.data.edit_bones.active.select = True
        bpy.ops.armature.duplicate_move()
        
        # #Change to pose mode
        # bpy.ops.object.mode_set(mode='POSE')
        
        # #Select all the deforming bones, which are on layer 2
        # bpy.context.object.data.layers[1] = True
        # bones = [b for b in bpy.context.active_object.pose.bones if b.bone.layers[1]]
        
        # bpy.ops.pose.select_all(action='DESELECT')
        # for b in bones:
        #     b.bone.select=True


        # #Loop in all actions
        # for a in bpy.data.actions:
            
        #     if not a:
        #         continue
            
        #     bpy.context.active_object.animation_data.action = a
            
        #     firstFrame = 9999999
        #     lastFrame = -9999999
            
        #     #Get the first and last keyframes of the current action
        #     for fcu in a.fcurves:
        #                 for keyframe in fcu.keyframe_points:
                            
        #                     x, y = keyframe.co
        #                     k = math.ceil(x)
                            
        #                     if k &lt; firstFrame:
        #                         firstFrame = k
                            
        #                     if k &gt; lastFrame:
        #                         lastFrame = k
            
        #     #Bake it
        #     bpy.ops.nla.bake(frame_start=firstFrame, frame_end=lastFrame, only_selected=True, visual_keying=True, clear_constraints=True, use_current_action=True, bake_types={'POSE'})
            
        #     print ("Action: {}, First frame: {}, Second frame: {}".format(a.name, firstFrame, lastFrame))
            
        return {'FINISHED'}

classes = (
    OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation
)

def register():    
    from bpy.utils import register_class
    cls = OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation
    # for cls in classes:
        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    cls = OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation
    # for cls in reversed(classes):
        unregister_class(cls)