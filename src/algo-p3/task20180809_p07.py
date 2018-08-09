# 入力した値が正しいかを判定する関数validateを定義してください
# (引数にhandを取り、戻り値に判定結果(正しければTrue,不正ならFalse)を返します。)


def validate(hand):
    '''
    じゃんけんで出した手の形を正しく出力させるための関数(0,1,2以外で構文エラーが出ないようにするもの)

    Parameters
    ----------
    hand
        じゃんけんで出した手の形

    Returns
    -------
    False
        不正入力
    True
        正しい入力
    '''
    # handが0より小さい、または2より大きい場合Falseを返してください
    # 上記以外の場合、Trueを返してください。
    if hand < 0:
        return False
    elif hand > 2:
        return False
    else:
        return True


def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得

    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        プレイヤーの名前(初期値はゲスト)

    Returns
    -------
    None
    '''
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')


print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数validateの戻り値がTrueの場合のみ、以下のif~else文が実行されるようにしてください
if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# 関数validateの戻り値がFalseの場合「正しい数値を入力してください」と出力してください
else:
    print("正しい数値を入力してください")
