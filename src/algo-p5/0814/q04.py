# 変数定義部
# 初期値10を持つ変数goal_posを定義してください。
goal_pos = 10
cur_pos = 0  # 現在の位置

# 関数定義部


def go_forward(cells):
    """
    前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

# 以下メイン処理
# 開始メッセージを表示


print("すごろくゲーム、Start!!")

# ゴールに到達するまで(cur_pos<goal_pos)、既存の処理を繰り返してください。
while cur_pos < goal_pos:
    # サイコロで出た目をdice_numに代入
    dice_num = 1

    # 出たサイコロの目を表示
    print(str(dice_num) + "の目が出ました。")

    # 出た目の分だけ進む
    go_forward(dice_num)

# 「ゴールしました。おめでとうございます!」を表示してください。
print("ゴールしました。おめでとうございます!")
