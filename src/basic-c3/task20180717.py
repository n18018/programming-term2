import random

# リストの作成
tenki = ["晴れ", "曇り", "雨"]
kion = [10, 20, 30, 40]
kousui = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# ランダムにリストから１つ選ぶ
a = random.randint(0, len(tenki)-1)
b = random.randint(0, len(kion)-1)
c = random.randint(0, len(kousui)-1)

# 出力
print("今日の天気は", tenki[a])
print("気温は", kion[b])
print("降水確率は", kousui[c])

# 結果には矛盾が生じる可能性があります。
