# 程序目标:
#   如果用户名存在就显示他
#   如果用户名不存在就提示用户输入
# 理解重构的真实意义

import json

# # version 0.1
# file = 'txt/name.json'
# try:
#     with open(file) as obj:
#         name = json.load(obj)
# except FileNotFoundError:
#     name = input("What's your name? ")
#     with open(file, 'a') as obj:
#         json.dump(name, obj)
#         print(f"We'll remember you when you come back, {name.title()}!")
# else:
#     print(f"Welcome back {name}!")


# # version 0.2
# 代码能够正确运行, 但可做进一步的改进--将代码划分为一系列完成具体工作的函数.
# 这样的过程被称为重构/refactor, 让代码更清晰, 更容易理解, 更容易扩展
# def greetUser():
#     """Say hello to user"""
#     file = "txt/name.json"
#     try:
#         with open(file) as obj:
#             name = json.load(obj)
#     except FileNotFoundError:
#         name = input("What's your name? ")
#         with open(file, 'a') as obj:
#             json.dump(name, obj)
#             print(f"We'll remember you when you come back, {name.title()}!")
#     else:
#         print(f"Welcome back {name}!")
#
#
# greetUser()


# version 0.3
# version 0.2 的代码只是将程序函数化, 这是面向过程编程常见的模式, 还称不上重构
# 下面拆分greetUser()让它不执行那么多任务, 按逻辑划分函数, 每个函数只执行单一任务
file = 'txt/name.json'


def getExistName():
    """Get exist username"""
    try:
        with open(file) as obj:
            name = json.load(obj)
    except FileNotFoundError:
        pass
    else:
        return name


def getNewName():
    """Get new username"""
    name = input("What's your name? ")
    with open(file, 'a') as obj:
        json.dump(name, obj)
    return name


def greetUser():
    """Say hello to user"""
    name = getExistName()
    if name:
        print(f"Welcome back {name.title()}!")
    else:
        name = getNewName()
        print(f"We'll remember you when you come back, {name.title()}!")


greetUser()

# 将所有的逻辑都分化到函数中, 每个逻辑步骤都由一个函数负责就是重构;
# 这么做对于当前简单小程序来说就是脱裤子放屁, 但设想一下, 如果是超大型程序呢?
# 重构的意义在于让代码:
#   更清晰
#   更容易理解
#   更容易扩展
#
# 按照重构的思想, 改变一下更现实一点的要求:
#   用户输入名称, 判断是否老用户
#       老用户致欢迎词
#       新用户指导注册
# 作业greetUser.py
