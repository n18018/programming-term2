# クラスの定義
class HumanName:
    '''人を表すクラス'''
    def setName(self, name):
        '''名前を設定するメソッド'''
        self.name = name

    def getName(self):
        '''名前を取得するメソッド'''
        return self.name


# インスタンスを生成
taro = HumanName()
taro.setName("taro")
print(taro.getName())

jiro = HumanName()
jiro.setName("jiro")
print(jiro.getName())
print(jiro.name)
