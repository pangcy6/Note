# 导入自定义类randWalkClass.py的主程序
import matplotlib.pyplot as plt
from randWalkClass import RandomWalk


rw = RandomWalk()
rw.fillWalk()
plt.scatter(rw.x_values, rw.y_values, s=2)
plt.show()
