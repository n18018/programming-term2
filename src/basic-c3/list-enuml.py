# for構文でenumerate()を使う
fruits = ["Apple", "Orange", "Banana"]
for i, v in enumerate(fruits):
    print(i, v)

# enumerate()の動作を確認する
fruits = ["Apple", "Orange", "Banana"]
print(list(enumerate(fruits)))
