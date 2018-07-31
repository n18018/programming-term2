import random
cur_x = 0

while True:
    if cur_x < 10:
        shake_dice = random.randint(1, 6)
        cur_x = cur_x + shake_dice
        input("サイコロを降ってください")
        print(shake_dice, "が出ました。", "現在位置は", cur_x, "です。")
    if cur_x > 10:
        shake_dice = random.randint(1, 6)
        cur_x = cur_x - shake_dice
        print("ゴールを超えているので逆走します。")
        input("サイコロを降ってください")
        print(shake_dice, "が出ました。", "現在位置は", cur_x, "です。")
    if cur_x == 10:
        break

print("おめでとうございます、ゴールしました!")
