from enemy import Enemy


class BossChara(Enemy):
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            敵の名前
        Returns
        -------
        自分自身のインスタンス
        """
        super().__init__(name)
        # self.hpを150、self.min_damageを7、self.max_damageを12、self.freqを15に変更してください。
        self.hp = 150
        self.min_damage = 7
        self.max_damage = 12
        self.freq = 15
