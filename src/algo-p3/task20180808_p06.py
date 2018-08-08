def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得

    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        じゃんけんのプレイヤー(初期値は'ゲスト')

    Returns
    -------
    None
    '''
    # 変数handsに、'グー','チョキ','パー'を要素に持つリストを代入してください
    hands = ['グー', 'チョキ', 'パー']

    # リストhandsを用いて、選択した手が出力されるように、(◯◯)の部分を書き換えましょう
    print(name + 'は', hands[player_hand], 'を出しました')


print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# 「何を出しますか？（0: グー, 1: チョキ, 2: パー）」と出力してください
print("何を出しますか？(0: グー, 1: チョキ, 2: パー)")

# inputを用いて「数字入力してください：」をコンソールに表示後、入力を受け取り、数値に型変換してから変数player_handに代入するよう変更してください
player_hand = int(input('数字で入力してください：'))

if player_name == '':
    # 第1引数を変数player_handに書き換えてください
    print_hand(player_hand)
else:
    # 第1引数を変数player_handに書き換えてください
    print_hand(player_hand, player_name)
