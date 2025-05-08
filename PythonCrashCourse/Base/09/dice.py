# 第一次尝试导入标准库中的模块 random, 其中 randint()返回指定范围内的一个随机整数. 用来模拟骰子的行为
from random import randint


class Dice():
    """模拟掷骰子"""

    def __init__(self, a, b):
        """初始化类属性"""
        self.a = a
        self.b = b

    def play(self):
        """模拟掷骰子游戏"""
        x = int(input(str(self.b) + "面的掷骰子游戏, 你想玩几次? "))
        for _ in range(x):
            print(f"点数: {randint(self.a, self.b)}")


dice = Dice(1, 6)   # 实例化标准样式
dice.play()
Dice(1, 10).play()  # 实例化+调用二合一, 代码更简洁
Dice(1, 20).play()

'''
这段小程序一开始就掉坑里了:
受教材影响, 开始敲代码之前就毫无怀疑的要继承random模块当中的类randint.
百转千回, 耗时几个小时, 才忽然明白: 为什么要继承? 程序需要的不过是一个随机数而已!
至此豁然开朗

教训: 直接聚焦要解决问题的本身, 要以解决问题为导向, 而不是选择哪一条技术路线.
'''
