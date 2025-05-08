import matplotlib.pyplot as plt
from random import choice   # 每次决策都使用choice()


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, numpoints=5000):   # 漫步次数 5000
        """初始化随机漫步的属性"""
        self.numpoints = numpoints
        # 随机漫步起始点
        self.x_values = [0]
        self.y_values = [0]

    def fillWalk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步, 直到列表达到指定的长度
        while len(self.x_values) < self.numpoints:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk()
rw.fillWalk()
plt.scatter(rw.x_values, rw.y_values, s=2)
plt.show()
