from random import randint


class Dice():
    """一个表示骰子的类"""

    def __init__(self, sides=6):
        """默认普通骰子6个面"""
        self.sides = sides

    def roll(self):
        """返回一个1到骰子面数之间的随机数"""
        return randint(1, self.sides)
