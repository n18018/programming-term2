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
    if hand < 0 or hand > 2:
        return False
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

if validate(player_hand):
    # 変数computer_handに数値1を代入してください
    computer_hand = 1

    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)

    # 第1引数をcomputer_hand、第2引数を文字列「コンピューター」とし関数print_handを呼び出してください
    print_hand(computer_hand, "コンピューター")

else:
    print('正しい数値を入力してください')
