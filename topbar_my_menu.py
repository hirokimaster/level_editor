import bpy

from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .spawn import MYADDON_OT_create_player_spawn_point_symbol
from .spawn import MYADDON_OT_create_enemy_spawn_point_symbol
from .create_event_trigger import MYADDON_OT_create_event_trigger

bl_info = {
    "name": "レベルエディタ",
    "author": "ryudai nihei",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

#トップバーの拡張メニュー
class TOPBAR_MT_my_menu(bpy.types.Menu):
    #Blenderがクラスを識別するための固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"
    #メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    #著者表示用の文字列
    bl_description = "拡張メニュー by" + bl_info["author"] 

    #サブメニューの描画
    def draw(self, context):
        #トップバーのエディタメニューに項目オペレータを追加
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname, text = MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname, text = MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname, text = MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_create_player_spawn_point_symbol.bl_idname, text=MYADDON_OT_create_player_spawn_point_symbol.bl_label)
        self.layout.operator(MYADDON_OT_create_enemy_spawn_point_symbol.bl_idname, text=MYADDON_OT_create_enemy_spawn_point_symbol.bl_label)
        self.layout.operator(MYADDON_OT_create_event_trigger.bl_idname, text=MYADDON_OT_create_event_trigger.bl_label)


    def submenu(self, context):
        #ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)