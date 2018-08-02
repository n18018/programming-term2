# メンバーとデータをリストに格納
menber = {
    'Aiba': 175,
    'Matsumoto': 172,
    'Ninomiya': 168,
    'Oono': 166,
    'Sakurai': 171
}


# リストの昇順ソート
for k, v in sorted(menber.items(), key=lambda x: x[1]):
    print(str(k) + ": " + str(v))
