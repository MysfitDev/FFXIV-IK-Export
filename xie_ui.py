import math
import textwrap

from . import (addon_updater_ops,
                xie_ops)
                       
from bpy.types import (Panel,
                        Operator,
                        )
                       
from mathutils import (Matrix,
                        Vector,
                        )

properties_bl_idname = "object.xiv_ik_exporter_hierarchy_props"

class OBJECT_PT_FFXIV_IK_Export_BakeFKRig(Panel):
    bl_label = 'FFXIV IK Export'
    bl_idname = 'XIE_PT_AssettoMaterialPanel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'XIV IK'
    
    def draw(self, context):
        props = self.layout.operator(properties_bl_idname)
        
        layout = self.layout
        scene = context.scene
        xie_tool = scene.xie_tool
        
        row = layout.row()
        row.prop(xie_tool, "ik_rig")
        row.prop(xie_tool, "fk_rig")
        
        row = layout.row()
        row.operator(xie_ops.OBJECT_OT_FFXIV_IK_Export_BakeIKAnimation.bl_idname)

classes = (
    OBJECT_PT_FFXIV_IK_Export_BakeFKRig
)

def register(properties_bl_idname):
    properties_bl_idname = properties_bl_idname
    
    from bpy.utils import register_class
    cls = OBJECT_PT_FFXIV_IK_Export_BakeFKRig
    # for cls in classes:
        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    cls = OBJECT_PT_FFXIV_IK_Export_BakeFKRig
    # for cls in reversed(classes):
        unregister_class(cls)
    
    properties_bl_idname = None