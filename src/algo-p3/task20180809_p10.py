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
    name-'ゲスト'
        プレイヤーの名前(初期値はゲスト)

    Returns
    -------
    None
    '''
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# 関数judgeを定義してください
# (引数にplayer(プレイヤーの出した手(0,1,2))とcomputer(コンピュータの出した手)を取り、
#  戻り値として、「勝ち」「負け」「引き分け」の文字列で結果を返します。)


def judge(player, computer):
    '''
    playerとcomputerの対戦結果を出力するための関数

    Parameters
    ----------
    player
        ユーザーが入力したじゃんけん
    computer
        プリセットされたじゃんけんを出力(1:チョキ固定)

    Returns
    -------
    "引き分け"
        playerとcomputerが出したものが同じであるため引き分け
    "勝ち"
        playerがcomputerに勝てる数値を入力したためplayerの勝ち
    "負け"
        playerがcomputerに負ける数値を入力したためplayerの負け
    '''
    # playerとcomputerが等しければ「引き分け」を返してください
    if player == computer:
        return "引き分け"
    # 上記に当てはまらず、(playerが0かつcomputerが1)または(playerが1かつcomputerが2)
    # または(playerが2かつcomputerが0)の場合、「勝ち」を返してください
    # ※elifを1回で上記を表現することが難しければ、elifを3回書いても構いません。
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2):
        return "勝ち"
    # 上記どちらにも当てはまらない場合は、「負け」を返してください。
    else:
        return "負け"


print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    computer_hand = 1

    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)

    print_hand(computer_hand, 'コンピューター')

    # 変数resultに関数judgeの戻り値を代入してください
    result = judge(player_hand, computer_hand)

    # 変数resultを、「結果は(result)でした」の形式で出力してください
    print("結果は", result, "でした")

else:
    print('正しい数値を入力してください')
