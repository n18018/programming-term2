# 値段
beer_v = 200
tumami_v = 100
yakitori_v = 100
# 焼鳥の割引率
yakitori_s = 1 - 0.2  # 2割引のため
# 個数
beer_c = 2
tumami_c = 1
yakitori_c = 2
# 値引き
nebiki = 150
# 計算
sum_v = ((beer_v * beer_c) + (tumami_v * tumami_c) + ((yakitori_v * yakitori_s)* yakitori_c)) - nebiki
# 結果を表示
print("会計は", sum_v, "円です")
