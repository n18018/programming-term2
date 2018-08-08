# 仮引数nameの初期値を「ゲスト」に設定してください
def print_hand(hand, name='ゲスト'):
    '''
    誰がじゃんけんで何を出したかを取得

    Parameters
    ----------
    hand
        じゃんけんで出した手の形
    name='ゲスト'
        じゃんけんのプレイヤー(初期値は'ゲスト')
    '''
    print(name + 'は' + hand + 'を出しました')

# 引数に文字列グーのみを入れてprint_hand関数を呼び出してください
print_hand('グー')
