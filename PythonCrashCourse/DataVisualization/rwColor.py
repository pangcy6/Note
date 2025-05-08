# 继续沿用上一个例子中的类文件

import matplotlib.pyplot as plt

from randWalkClass import RandomWalk

# 只要程序处于活动状态, 就不断地模拟随机漫步
while True:
    # 创建一个 RandomWalk 实例, 并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fillWalk()

    pointnumbers = list(range(rw.numpoints))
    plt.scatter(rw.x_values, rw.y_values, c=pointnumbers,
                cmap=plt.cm.Blues, edgecolor='none', s=5)

    # 突出显示起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolor='none', s=50)

    plt.show()

    keepRuning = input("Make another walk? (y/n): ")
    if keepRuning == 'n':
        break
