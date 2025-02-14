import bpy

#オペレータ 移動ルート生成
class MYADDON_OT_create_move_route(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_move_route"
    bl_label = "移動ルート生成"
    bl_description = "移動ルートを生成します"
    #リドゥ、アンドゥ可能オプション
    bl_options = {'REGISTER', 'UNDO'}

    #メニューを実行したときに呼ばれるコールバック関数
    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_path_add()
        print("移動ルートを生成しました")

        # 作成したオブジェクトを取得
        obj = bpy.context.object
        obj.name = "移動ルート"

        # オペレータの命令終了を通知
        return {'FINISHED'}