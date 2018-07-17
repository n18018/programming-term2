print('  |  1  2  3  4  5  6  7  8  9')
print("--+---------------------------")
for x in range(1, 10):
    print(str(x), '|', end="")
    for y in range(1, 10):
        print("%3d" % (x * y), end="")
    print('')

# 3行目はネットの情報を参考
# ここまで出来ました。
