# 変数
my_hand = int(input("何を出しますか? 1:グー 2:チョキ 3:パー => "))
case_1 = "CPUがパーを出しました。あなたの負けです。"
case_2 = "CPUがグーを出しました。あなたの負けです。"
case_3 = "CPUがチョキをだしました。あなたの負けです。"

# 勝負とその結果
if my_hand == 1:
    print(case_1)
elif my_hand == 2:
    print(case_2)
else:
    print(case_3)
