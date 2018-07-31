import sys

# メインメニュー
main = {'DripCoffee': 280,
        'ColdBrewCoffee': 320,
        'CafeLatte': 330,
        'SoyLatte': 380,
        'Cappuccino': 330,
        'CaramelFrappuccino': 470,
        'MacchaCreamFrappuccino': 470}

# オプション
op = {'LowFatMilk': 0,
      'NonFatMilk': 0,
      'SoyMilk': 50,
      'DeepCoffee': 60,
      'WhipCream': 70,
      'CaramelShrup': 60,
      'ChocoSource': 0,
      'DeCafe': 50}

# オーダーリスト
a_order = []
sum_v = 0

# オーダー開始
while True:
    order_1 = input("メインメニューを選んでください。")
    if order_1 in main:
        sum_v += main[order_1]
        print("メインメニューを承りました。")
        break
    elif order_1 == "" or order_1 == "q":
        print("注文がキャンセルされました。")
        sys.exit(0)
    else:
        print("選択されたメニューはありません")

while True:
    order_2 = input("オプションメニューを選んでください。")
    if order_2 in op:
        a_order.append(order_2)
        sum_v += op[order_2]
        print("他にオプションメニューの注文はございますか?")
    elif order_2 == "" or order_2 == "q":
        break
    else:
        print("選択されたオプションはありません。\n"
              "他にオプションメニューの注文はございますか?")

# 注文内容の確認
print("注文内容は[", order_1, a_order, "]です。")
print("合計金額は", sum_v, "円です。")
print("右奥のカウンターにてお待ちください。")
