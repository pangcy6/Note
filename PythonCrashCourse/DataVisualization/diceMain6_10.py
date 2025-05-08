from diceClass import Dice
import pygal

# 创建一个D6一个D10
dice6 = Dice()
dice10 = Dice(10)

# 掷, 结果存储到列表中
results = []
for rollNum in range(50000):
    result = dice6.roll() + dice10.roll()
    results.append(result)

# 分析
frequencies = []
maxResult = dice6.sides + dice10.sides
for value in range(2, maxResult+1):
    frequencies.append(results.count(value))

# 可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = list(range(2, 16))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('image/diceVisual6_10.svg')
