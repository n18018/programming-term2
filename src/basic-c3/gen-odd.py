# 30以下の奇数を返すイテレータ
def gen0dd():
    i = 1
    while i <= 30:
        yield i
        i += 2

# イテレータを得る


it = gen0dd()
for v in it:
    print(v, end=",")
