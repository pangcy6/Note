import pygal

from diceClass import Dice

# 创建两个D6骰子
dice1 = Dice()
dice2 = Dice()

# 多次掷骰子, 将结果存到一个列表里
results = []
for _ in range(1000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# 分析结果
frequencies = []
maxResult = dice1.sides + dice2.sides
for value in range(2, maxResult+1):
    frequencies.append(results.count(value))

# 可视化
hist = pygal.Bar()
hist.title = "掷两个6面骰子1000次的结果"
hist.x_labels = list(range(2, maxResult+1))
hist.x_title = "点数"
hist.y_title = "出现频次"

hist.add('两个6面骰子', frequencies)
hist.render_to_file('image/dice2Visual.svg')
