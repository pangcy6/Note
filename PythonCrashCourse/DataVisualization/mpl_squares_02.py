import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49]
plt.plot(squares, linewidth=5)

# 设置图表标题, 坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
