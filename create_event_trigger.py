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
