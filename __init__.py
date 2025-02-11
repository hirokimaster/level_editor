import bpy


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

#モジュールのインポート
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .add_collider import MYADDON_OT_add_collider
from .add_filename import MYADDON_OT_add_filename
from .draw_collider import DrawCollider
from .export_scene import MYADDON_OT_export_scene
from .disabled import MYADDON_OT_add_disabled
from .disabled import OBJECT_PT_disabled
from .spawn import MYADDON_OT_spawn_point_symbol
from .spawn import MYADDON_OT_create_spawn_point_symbol
from .spawn import MYADDON_OT_create_player_spawn_point_symbol
from .spawn import MYADDON_OT_create_enemy_spawn_point_symbol


#メニュー項目描画
def draw_menu_manual(self, context):
    #self : 呼び出し元のクラスインスタンス。C++でいうthisポインタ
    #context : カーソルを合わせた時のポップアップのカスタマイズなどに使用

    #トップバーのエディタメニューに項目オペレータを追加
    self.layout.operator("wm.url_open_preset", text = "Manual", icon = "HELP")

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
        self.layout.operator(MYADDON_OT_create_enemy_sortieroad.bl_idname, text = MYADDON_OT_create_enemy_sortieroad.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname, text = MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_create_player_spawn_point_symbol.bl_idname, text=MYADDON_OT_create_player_spawn_point_symbol.bl_label)
        self.layout.operator(MYADDON_OT_create_enemy_spawn_point_symbol.bl_idname, text=MYADDON_OT_create_enemy_spawn_point_symbol.bl_label)


    def submenu(self, context):
        #ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)


class MYADDON_OT_create_enemy_sortieroad(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_enemy_sortieroad"
    bl_label = "曲線を生成"
    bl_description = "2点の曲線オブジェクトを生成します"
    bl_options = {'REGISTER', 'UNDO'}

    # 制御点1と制御点2の位置をユーザーに入力させるためのプロパティ
    point1: bpy.props.FloatVectorProperty(
        name="Point 1",
        description="最初の制御点の位置",
        default=(0.0, 0.0, 0.0),
        subtype='TRANSLATION'
    ) # type: ignore

    point2: bpy.props.FloatVectorProperty(
        name="Point 2",
        description="2番目の制御点の位置",
        default=(1.0, 0.0, 0.0),
        subtype='TRANSLATION'
    ) # type: ignore

    def create_curve(self, context):
        # 曲線データの生成
        curve_data = bpy.data.curves.new(name="EnemySortieRoad", type='CURVE')
        curve_data.dimensions = '3D'

        polyline = curve_data.splines.new(type='POLY')
        polyline.points.add(1)  # 1点追加して2点にする

        # プロパティの値を取得
        point1 = self.point1
        point2 = self.point2

        polyline.points[0].co = (point1[0], point1[1], point1[2], 1)  # W成分を含める
        polyline.points[1].co = (point2[0], point2[1], point2[2], 1)  # W成分を含める

        # 曲線オブジェクトを作成してシーンに追加
        curve_object = bpy.data.objects.new("EnemySortieRoad", curve_data)
        context.collection.objects.link(curve_object)

    def execute(self, context):
        self.create_curve(context)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    
#パネル ファイル名
class OBJECT_PT_file_name(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_file_name"
    bl_label = "FileName"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):
        #パネルに項目を追加
        if "file_name" in context.object:
            #既にプロパティがあれば、プロパティ表示
            self.layout.prop(context.object, '["file_name"]', text = self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_filename.bl_idname)
           
#パネル コライダー
class OBJECT_PT_collider(bpy.types.Panel):
    bl_idname = "OBJECT_PT_collider"
    bl_label = "Collider"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):

        #パネルに項目を追加
        if "collider" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layuout.prop(context.object, '["collider]', text = "Type")
            self.layuout.prop(context.object, '["collider_center]', text = "Center")
            self.layuout.prop(context.object, '["collider_size]', text = "Size")
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_collider.bl_idname)


#blenderに登録するクラスリスト
classes = (MYADDON_OT_create_ico_sphere,
           MYADDON_OT_stretch_vertex,
           TOPBAR_MT_my_menu,
           MYADDON_OT_export_scene,
           OBJECT_PT_file_name,
           MYADDON_OT_add_filename,
           MYADDON_OT_add_collider,
           OBJECT_PT_collider,
           MYADDON_OT_create_enemy_sortieroad,
           MYADDON_OT_add_disabled,
           OBJECT_PT_disabled,
           MYADDON_OT_spawn_point_symbol,
           MYADDON_OT_create_spawn_point_symbol,
           MYADDON_OT_create_player_spawn_point_symbol,
           MYADDON_OT_create_enemy_spawn_point_symbol,
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

