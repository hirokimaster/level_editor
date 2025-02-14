import bpy

#オペレータ イベントトリガー
class MYADDON_OT_create_event_trigger(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_event_trigger"
    bl_label = "イベントトリガー生成"
    bl_description = "イベントトリガーを生成します"
    #リドゥ、アンドゥ可能オプション
    bl_options = {'REGISTER', 'UNDO'}

    #メニューを実行したときに呼ばれるコールバック関数
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object
        obj.name = "EventTrigger"  # 名前を設定

        # イベント用のカスタムプロパティを追加
        obj["event_id"] = 1  # イベント番号（デフォルト: 1）

        print(f"イベントトリガーを生成しました: イベントID: {obj['event_id']}")

        #オペレータの命令終了を通知
        return {'FINISHED'}


#オペレータ カスタムプロパティ['event_id']追加
class MYADDON_OT_add_event_id(bpy.types.Operator):
    bl_idname = "myaddon.myaddo_ot_add_event_number"
    bl_label = "イベント番号 追加"
    bl_description = "['event_id']カスタムプロパティを追加します"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        #['event_id']カスタムプロパティを追加
        context.object["event_id"] = 0 #初期はゼロ

        return {"FINISHED"}
    

#パネル イベント番号
class OBJECT_PT_event_id(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_event_id"
    bl_label = "イベント番号"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):
        #パネルに項目を追加
        if "event_id" in context.object:
            #既にプロパティがあれば、プロパティ表示
            self.layout.prop(context.object, '["event_id"]', text = self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_event_id.bl_idname)