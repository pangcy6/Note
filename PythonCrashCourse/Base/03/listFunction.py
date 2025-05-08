
# 列表的增删改查

names = ['赵', '钱', '孙', '李']
print(names)  # 基本上很少直接打印列表

# 增(末尾)
names.append('吴')
print(names)

# 增(指定位置)
# names = names.insert(-2, '周'), 这种写法没道理, 当然是错误的.
names.insert(4, '周')
print(names)
print(names[-1])

# 彻底删除
del names[4]
print(names)

# 弹出
# 默认弹出最后一个元素, 也可指定弹出元素
names.pop()
print(names)

names.pop(1)
print(names)

names.insert(1, '钱')
print(names)

# 按元素名称删除
names.remove('钱')
print(names)

# 改
names[-1] = '周'
print(names)

# 查
message = "百家姓第一个姓是: " + names[0] + "."
print(message)
