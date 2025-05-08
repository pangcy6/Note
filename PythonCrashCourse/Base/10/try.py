print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input("\nSecond number: ")
    if second == 'q':
        break

    try:
        answer = float(first) / float(second)
    except ZeroDivisionError:
        print("You can't divede by 0!")
    else:
        print(answer)

"""
小结:
    为这个小程序纠结了许久许久, 一直想着排查所有的非法输入结果发现根本做不到
    开始还以为可以利用 Python 内置函数来解决问题, 结果是无效
    直到今天2023-12-20才突然意识到我们还有正则表达式
    等学完了正则表达式再回来跟丫死磕
"""
