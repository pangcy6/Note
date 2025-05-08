# json两个基本功能:
#   json.dump()写入
#   json.load()读取
# 这段程序略显无聊, 但如果把它拆成两个程序, 那么就是不同程序间共享数据.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'txt/numbers.json'
with open(filename, 'w') as obj:
    json.dump(numbers, obj)

with open(filename) as f_obj:
    num = json.load(f_obj)

print(num)
