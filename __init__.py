bl_info = {
    "name": "FFXIV IK Exporter",
    "author": "Jesse Myers",
    "description" : "Provides useful tools creating and exporting IK Animations to FFXIV Skeletons",
    "blender": (2, 80, 0),
    "category": "Object",
    "version": (0, 1, 0, 0)
}

import bpy
import math
import textwrap

from . import (addon_updater_ops,
                xie_ui,
                xie_ops)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
                       
from bpy.types import (AddonPreferences,
                       PropertyGroup,
                       )
                       
from mathutils import Matrix
from mathutils import Vector

class XIE_Addon_Properties(PropertyGroup):
    bl_idname = "object.xiv_ik_exporter_hierarchy_props"
    bl_label = "Property Example"
    bl_options = {'REGISTER', 'UNDO'}
        
    ik_rig: PointerProperty(
        type = bpy.types.Object,
        name = "IK Rig"
        )
        
    fk_rig: PointerProperty(
        type = bpy.types.Object,
        name = "FFXIV Rig"
        )
     
    
    def execute(self, context):
        self.report({'INFO'}, self.collection_name)
        return {'FINISHED'}

@addon_updater_ops.make_annotations
class XIE_Addon_Preferences(AddonPreferences):
    """Demo bare-bones preferences"""
    bl_idname = __package__

    # Addon updater preferences.

    auto_check_update = bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False)

    updater_interval_months = bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0)

    updater_interval_days = bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31)

    updater_interval_hours = bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23)

    updater_interval_minutes = bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59)

    def draw(self, context):
        layout = self.layout
        mainrow = layout.row()
        col = mainrow.column()
        addon_updater_ops.update_settings_ui(self, context)
        
classes = (
    XIE_Addon_Preferences,
    XIE_Addon_Properties,
)

def register():
    addon_updater_ops.register(bl_info)
    
    from bpy.utils import register_class
    for cls in classes:
        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        register_class(cls)
        
    xie_ops.register()
    xie_ui.register(XIE_Addon_Properties.bl_idname)
    
    bpy.types.Scene.xie_tool = PointerProperty(type=XIE_Addon_Properties)

def unregister():
    # Addon updater unregister.
    addon_updater_ops.unregister()
    
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls) 
        
    xie_ops.unregister()
    xie_ui.unregister()
    
    del bpy.types.Scene.xie_tool
