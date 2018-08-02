# メンバーとデータをリストに格納
menber = {
    'Aiba': 35,
    'Matsumoto': 34,
    'Ninomiya': 35,
    'Oono': 37,
    'Sakurai': 36
}


# リストの降順ソート
for k, v in sorted(menber.items(), key=lambda x: x[1], reverse=True):
    print(str(k) + ": " + str(v))
