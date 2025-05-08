
# # 第一版: 逻辑错误, 暂时还找不到错误的原因
# orders = ['干煸豆角', '鱼香肉丝', '软烧茄子', '辣子鸡块', '鸡蛋豆腐汤']
# finished = []
#
# for order in orders:
#     # order = orders.pop()  # 这里就是错误原因
#     print(f"您的{order}正在制作...")
#     finished.append(order)
#
# print("\n您的订单已经完成, 祝您用餐愉快!")
# for order in finished:
#     print(f"\t{order}")

"""
错误解析:
    1. 没有理解 for...in 循环的本质
    2. 要达到原程序要求, 两个列表根本没有必要

程序优化之后的代码:
"""

orders = ['干煸豆角', '鱼香肉丝', '软烧茄子', '辣子鸡块', '鸡蛋豆腐汤']

for order in orders:
    print(f'您的{order}正在制作...')

print('\n您的订单已经完成, 祝您用餐愉快!')

for order in orders:
    print(f'\t{order}')

print("-" * 20 + "while" + "-" * 20)

# while实现
# 显然 while 循环实现起来略显繁琐
# 相对来说 for 循环更适合这类特定步骤的循环
# while 更适合区间判断的场合
# 不僵化是程序员的基本素养
finished = []
while orders:
    a = orders.pop(0)
    print(f"您的{a}正在制作...")
    finished.append(a)

print('\n您的订单已经完成, 祝您用餐愉快!')

while finished:
    print(f"\t{finished[0]}")
    del finished[0]
