# 查看文件的第一行
import csv

from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # 创建csv的阅读器(仅打开, 还未读)
    reader = csv.reader(f)
    # 将阅读器传递给next(), 它将返回下一行
    header_row = next(reader)
    # 获取表头, 了解文件结构
    # print(header_row)

    # 从文件中获取最高气温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    # print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))      # figure函数用法去官网查询
    plt.plot(highs, c='red')

    # 设置图形格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
