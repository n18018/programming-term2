r1 = range(1, 41)

print(list(filter(lambda x: (x % 3) == 0 or
                  (x // 10) == 3 or (x % 10) == 3, r1)))


# line基準を超えないよう改行してあります
