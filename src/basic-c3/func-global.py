#  関数の外側でvalueに100を代入
value = 100


def changeValue():
    '''
    グローバル変数の値を変更する。

    Parameters
    ----------
    none

    returns
    -------
    none
    '''
    #  valueをグローバル宣言
    global value
    #  関数の内側でvalueを変更
    value = 20


changeValue()
print("value=", value)