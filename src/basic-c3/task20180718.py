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

# オーダー開始
order_1 = input("メインメニューを選んでください。")
if order_1 == [main]:
    print("メインメニューを承りました。")
else:
    print("選択されたメニューはありません")

while True:
    order_2 = input("オプションメニューを選んでください。")
    if order_2 == [op] or order_2 == "q": break
        print("他にオプションメニューの注文はございますか?")
    else:
        print("選択されたオプションはありません"
              "他にオプションメニューの注文はございますか?")

# まだ動かないのですがここまで出来ました
