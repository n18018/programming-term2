# 金額をリストに格納・変数の作成
money = [13600, 14500, 16000, 11111, 11667]
TAX_RATE = 10

# 税率の変数の作成
t10 = lambda t: round(t * (1 + TAX_RATE / 100))

# 結果の出力
print(list(map(t10, money)))
