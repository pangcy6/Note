"""
对于数字型列表来说:
    列表元素内的最大值: max(listName)
    最小值: min(listName)
    所有元素之和: sum(listName)
"""
#million = []
#for value in range(1, 1000001):
#	million.append(value)

#for i in million:
#	print(i)

million = list(range(1, 1000001))

print(f"列表的最大值为: {max(million)}.")
print(f"列表的最小值为: {min(million)}.")
print(f"列表的和为: {sum(million)}.")

#手动运算和
sum = 0
for i in million:
	sum += i
print(f"手动计算和为: {sum}")
