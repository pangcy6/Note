# range()步长参数
numbers = list(range(1, 11, 2))
print("打印1~10之间的奇数:")
for i in numbers:
    print(i)

time3 = list(range(3, 31, 3))
print("打印30以下能被3整除的数字:")
for i in time3:
    print(i)

# time3的另一种实现
time3_1 = list(range(1, 11))
for i in time3_1:
    print(3 * i)

# 立方
print("打印1-10的立方值:")
cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

# 立方解析
cubes_1 = [cube**3 for cube in range(1, 11)]
print(cubes_1)

# 切片
print("打印上述最后三个数字:")
for cube in cubes_1[-3:]:
    print(cube)
