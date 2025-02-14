import bpy

#モジュールのインポート
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .add_collider import MYADDON_OT_add_collider
from .add_collider import OBJECT_PT_collider
from .add_filename import MYADDON_OT_add_filename
from .add_filename import OBJECT_PT_file_name
from .draw_collider import DrawCollider
from .export_scene import MYADDON_OT_export_scene
from .disabled import MYADDON_OT_add_disabled
from .disabled import OBJECT_PT_disabled
from .spawn import MYADDON_OT_spawn_point_symbol
from .spawn import MYADDON_OT_create_spawn_point_symbol
from .spawn import MYADDON_OT_create_player_spawn_point_symbol
from .spawn import MYADDON_OT_create_enemy_spawn_point_symbol
from .create_event_trigger import MYADDON_OT_create_event_trigger
from .create_event_trigger import MYADDON_OT_add_event_id
from .create_event_trigger import OBJECT_PT_event_id
from .topbar_my_menu import TOPBAR_MT_my_menu
from .create_move_route import MYADDON_OT_create_move_route

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

#メニュー項目描画
def draw_menu_manual(self, context):
    #self : 呼び出し元のクラスインスタンス。C++でいうthisポインタ
    #context : カーソルを合わせた時のポップアップのカスタマイズなどに使用

    #トップバーのエディタメニューに項目オペレータを追加
    self.layout.operator("wm.url_open_preset", text = "Manual", icon = "HELP")


#blenderに登録するクラスリスト
classes = (MYADDON_OT_create_ico_sphere,
           MYADDON_OT_stretch_vertex,
           TOPBAR_MT_my_menu,
           MYADDON_OT_export_scene,
           OBJECT_PT_file_name,
           MYADDON_OT_add_filename,
           MYADDON_OT_add_collider,
           OBJECT_PT_collider,
           MYADDON_OT_add_disabled,
           OBJECT_PT_disabled,
           MYADDON_OT_spawn_point_symbol,
           MYADDON_OT_create_spawn_point_symbol,
           MYADDON_OT_create_player_spawn_point_symbol,
           MYADDON_OT_create_enemy_spawn_point_symbol,
           MYADDON_OT_create_event_trigger,
           MYADDON_OT_add_event_id,
           OBJECT_PT_event_id,
           MYADDON_OT_create_move_route
           )

#アドオン有効化時コールバック
def register():
    #blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました")

#アドオン無効化時コールバック
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    #blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    print("レベルエディタが無効化されました")
    
#テスト用実行コード
if __name__ == "__main__":
    register()

