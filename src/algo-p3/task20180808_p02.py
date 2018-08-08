# print_hand関数に、引数handを受け取れるように書き換えてください(handは文字列型の想定で構いません)
def print_hand(hand):
    '''
    じゃんけんで出したものを取得

    Parameters
    ----------
    hand
        出した手の形
    '''
    # 「(hand)を出しました」と、メッセージ中に引数handが出力されるように書き換えてください
    print(hand, "を出しました")

# 引数に文字列グーを入れて、print_hand関数を呼び出してください
print_hand('グー')

# 引数を文字列パーとして、print_hand関数を呼び出してください
print_hand('パー')
