# 再起関数を定義
def say_hello(i):
    '''関数の説明'''
    if i <= 0:
        print("ハロー", i)
        say_hello(i-1)

# 実行


say_hello(10)

help(say_hello)
