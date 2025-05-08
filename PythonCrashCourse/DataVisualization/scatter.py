# 第一个实用的散点图

import matplotlib.pyplot as plt

xValues = range(1, 1001)
yValues = [x ** 2 for x in xValues]
# 定义颜色和删除数据点轮廓色, 具体细节参考官网
plt.scatter(xValues, yValues, c=yValues,
            cmap=plt.cm.Reds, edgecolor='none', s=2)

plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('image/scatterColor.png')
