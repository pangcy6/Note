import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5, 6, 7]
squares = [1, 4, 9, 16, 25, 36, 49]
plt.plot(values, squares, linewidth=5)

# 设置图表标题, 坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
