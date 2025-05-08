from diceClass import Dice
import pygal

# 创建一个D6
dice = Dice()

# 掷骰子1000次将结果存储在一个列表内
results = []
for _ in range(1000):
    results.append(dice.roll())

# 分析结果
frequencies = []
for value in range(1, dice.sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

"""
frequency   -- 频率/频次
title       -- 整个图形标题
x_labels    -- x轴刻度
x/y_title   -- 坐标轴标题
"""
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1, 7))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('image/diceVisual1000.svg')
