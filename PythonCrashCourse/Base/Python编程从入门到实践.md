# Python编程从入门到实践

Author: Eric Mattes    Translator: 袁国忠

Date: 2023/06/02

---

<mark>不会按部就班, 必要性原则, 如有遗漏请参考原书.</mark>

## 2. 变量和简单数据类型

变量名命名规范:

- 变量名只能包含字母, 数字, 下划线; 允许使用字母或下划线开头, 但不能以数字开头

- 不能将Python关键字和函数名用作变量名

- 变量名应当既简短又具有描述性

- 慎用小写字母l和大写字母O, 容易被错看成数字1和0

[简单消息练习code](02/simpleMessage.py)

### 2.1 字符串

字符串是python中数据类型之一，表现形式为单引号或双引号括起的若干字符。

关于字符串的引号问题:

- 原则上逻辑清晰不能有含混不清的情况出现

- 特殊情况下, 要善用"\"转义符

- 一般情况下推荐双引号

处理大小写的三个方法:

1. str.title()

2. str.upper()

3. str.lower()

合并/拼接字符串: "+"

换行符与制表符在简单行的使用:

```python
>>> print("Language:\n\tPython\n\tC\n\tJavaScript")
Language:
    Python
    C
    JavaScript
```

如果内容复杂格式多样，那就要用到三引号字符串格式，
可以很好的保持格式见[示例](./02/format.py)

在Python中'string'和' string'是两个不同的字符串, 故:
删除字符串两侧空白的三个方法:

1. rstrip()--右

2. lstrip()--左

3. strip()--两侧

### 2.2 数字

支持的算法:

- \+ 加
- \- 减
- \* 乘
- / 除
- % 取余
- **    幂

**规则之一**: 只要有浮点数参与的运算, 则结果返回浮点数.

[四则运算示例](./02/calculate.py)

数据类型转换函数:

- str()

- int()

- float()

关于注释: <mark>新手期容易写语法注释,成熟的程序员的注释标准:是否可作为伪代码.</mark>

Python 之禅:

```python
import this
```

## 3. 列表

列表由一系列按特定顺序排列的元素组成, 可将任何东西加入列表, 元素之间可以没有任何关系; 列表名一般为复数形式.
表现形式如下:

`['trek', 'cannondale', 'redline', 'specialized', 12, True]`

列表是动态可变的数据类型, 列表的增删改查的方法:

- 改是直接赋值: list[0] = 'foo'

- 添加:
  
  - 末尾添加: list.append('some_foo')
  
  - 任意位置添加: list.insert(3, 'some_foo')

- 删除: 
  
  - 彻底删除, 以后无法访问: del list[2]
  
  - 删除后继续使用它的值(一般用于变化的过程中,如炸弹消失后的爆炸效果): list.pop()
    
    - pop()应该翻译为弹出, 它默认弹出列表最后一个元素
    
    - pop(2)是弹出第三个元素, 索引从0开始计数
  
  - 根据数值删除: list.remove('some_foo'), 同样也可以接着使用这个值
  
  - 判断标准:
    
    - 删除元素后不再以任何方式使用它, 那么del list[n]
    - 删除元素后还要继续使用它, 那么list.pop()或list.remove('foo')

- 查: 就是直接索引查

*注意点*:

- list[-1]表示最后一个元素, 负数的写法只适用于列表单个元素, 不适用于增删改查方法

[练习示例](./03/listFunction.py)

### 3.1 组织列表

永久性排序: list.sort()

永久性逆序: list.sort(reverse=True)

临时排序: sorted(list)
    此时print(list)还是原来的无序排列
    相当于新建了一个变量存储排序

反转列表(注意是反转不是排序): list.reverse()

两次反转恢复原貌

列表长度: len(list)

[wishlist.py](./03/wishlist.py)

**注意:** 操作列表时一个常见的错误为IndexError, 由索引越界引起.
解决办法:

1. 末尾元素索引改用-1 
2. 检查列表长度len(list)

## 4. 操作列表

for...in循环一般形式:

```python
for item in list_of_items:
    pass
```

<mark>在Python中冒号, 缩进是控制逻辑关系的外在表现</mark>, 不能出错.
<mark>空白行是业内约定, 分隔不同部分, 提高可读性, 语言本身不强制.</mark>

### 4.1 数值列表

函数range(n, m)实际是创建了一个从n开始至m-1的整数列表, 标准写法:

`numbers = list(range(1,6))` 得到 `[1, 2, 3, 4, 5]`

针对数值列表的统计计算:

- min(numbers)

- max(numbers)

- sum(numbers)

列表解析:

```python
# 一般模式
squares = []
for value in range(1,11):
    squeares.append(value**2)
print(squares)

# 列表解析:
squares = [value**2 for value in range(1, 11)]
print(squares)
```

[百万列表练习代码](./04/million.py)

[其他练习](./04/other.py)

### 4.2 切片--列表的一部分

- players[1:4] -- 第二个参数类似range()

- players[:5] -- 从头开始到第6个(不含)结束

- players[2:] -- 从2号开始到结尾全部

- players[-3:] -- 列表最后三个元素  

- players[:] -- 整个列表的切片, 用于复制列表

遍历切片:

```python
...
for player in players[:3]:
    print(player.title())
```

[示例](./04/other.py)

### 4.3 元组tuple

列表是可变数据类型, 某些不可变的数据就需要一种新的数据类型--元组.

如矩形边长: `dimensions = (20, 50)`, 可以取用`dimensions[0]`, 但不能修改.

遍历元组元素与列表类似.

虽然元组内元素不可变, 但可以重新赋值整个元组, 所以:

<mark>元组一般用于一组值在程序的整个生命周期内都不会改变的情况.</mark>

```python
# 元组tuple
menuInSchool = ('鱼香肉丝', '麻婆豆腐', '回锅肉', '宫保鸡丁', '酸菜鱼')
# menuInSchool[1] = '重庆辣子鸡'    # 不允许的操作,元组元素不可修改
for food in menuInSchool:
    print(food)

# 重新赋值, 允许操作, 在内存层面重新分配资源给变量; 现实世界厨师团队换了.
menuInschool = ('小葱拌豆腐', '京酱肉丝', '猪肉炖白菜', '苦瓜肉片')
```

### 4.4 代码格式

代码被阅读的机会远远大于编写的机会; 整洁规范的代码风格不仅仅是为了美观, 更容易协作和理解.

- 冒号与缩进是语言本身强制要求, Python 利用这个形式控制逻辑关系.
- 行长不超过 80 字符,利于多文件比对.
- 不同代码块之间适当的空行分隔, 逻辑与形式和谐统一.

## 5. if语句

每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。Python 根据条件测试的值为True还是False来决定是否执行if语句中的代码。如果条件测试的值为True， Python就执行紧跟在if语句后面的代码;如果为False，Python就忽略这些代码。

比较符号: (比较符号形成的表达式一律返回布尔值)

- 相等: ==

- 不相等: !=

- 小于: <

- 小于等于: <=

- 大于: >

- 大于等于: >=

**注意**: 字符串比较中, 可用lower()方法忽略大小写, 简化代码.

多个条件逻辑关系:

与: and

或: or

非: not

判断某一特定元素是否在列表中: `John in players`

if语句全模式:

```python
if conditional_test_1:
    do something
elif conditional_test_2:
    do something
elif ...
else:
    do something
```

特点: <mark>只会执行一条分支当中的语句 -- 条件符合就执行其余的忽略; 其中的关键点在于: 条件之间顺序的合理性</mark>

例如一个分年龄门票价格:

```python
age = 12

if age < 4:
    print("Your admission cost is free!")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 上述代码有大量重复,所以有优化的空间
# 从另一个角度来说, 凡是代码重复皆可优化
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f"Your admission cost is ${price}.")
```

<mark>else的潜在危险!</mark>
else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。

### 5.1 多个条件

有时多个条件都为True,都需要执行, 那么就使用一系列独立的if语句:

```python
...
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

上述代码很呆板, 用for循环很棒, 不过是为了展示if多条件的情形.

凡涉及用户输入, 防御性编程就是必要, 比如确定列表是否为空:

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

多个列表:

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
```

[一个新用户注册的示例](./05/signUp.py)

## 6. 字典

字典类似于列表, 但让你能够将不同的信息关联起来形成键值对(key/value), 可以更为准确的为各种真实物体建模, 形式如下:

`dict = {key1: value1, key2: value2, ... keyn: valuen}`

与key关联的value可以是数字, 字符串, 列表乃至字典, 事实上可将任何Python对象用作字典中的值.

字典和列表相比:
- 字典查询速度更快, 但占用资源多
- 列表占用资源少, 但速度慢
字典是典型的用空间换时间, 对于现代计算机来说, 资源已经不是瓶颈了, 效率才是!

举个栗子:

```python
# 重点是字典元素的增删改查

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',   # 推荐最后一个也加上",", 为以后在下一行添加键值对时做好准备
}

# 查询某个键值对
#print(f"Sarah's favorite language is {favorite_languages['sarah']}.")
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")
# 添加键值对
favorite_languages['john'] = 'php'
#修改键值对
favorite_languages['sarah'] = 'go'
print(favorite_languages)
# 删除
del favorite_languages['john']
print(favorite_languages)

# 遍历字典, 同时便利 key 和 value 注意标志为items()
# 单独遍历 value 标志为 keys()
for name, language in favorite_languages.items():
    print(name.title() + 
        "'s favorite language is " + 
        language.title() + 
        ".")
```

### 6.1 遍历字典

基本格式见上例中最后的代码.
全部格式见[遍历类型示例](./06/traverse.py)

**注意**: 遍历字典时, 键值对返回顺序与存储可能不同, Python只关心键和值之间的关联关系.

```python
#遍历字典中的键
for name in favorite_languages.keys():
    print(name.title())

# 遍历字典的特殊方式, 关键点在于取key和value的不同.
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
# 注意最后一行代码取key值和value值的不同!!!

# 单独遍历值
for v in dictory.values():
    print(v.title())
# 去除大量重复项
for v in set(dictory.values()):
    print(v.title())
# set()是集合数据类型,类似于列表,但每个元素必须独一无二
```

方法keys()并非只能用于遍历, 实际上它返回一个列表, 其中包含字典中所有的键.

按顺序遍历字典中所有键:

`for name in sorted(favorite_languages.keys()):`

字典遍历最简记忆:
- 全遍历: `for k, v in dict.items():`
- 键遍历: `for k in dict.keys():`
- 值遍历: `for v in dict.values():`


### 6.2 嵌套

有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print('Total number of aliens: ' + str(len(aliens)))
```

这些alien都有相同的特征, 在Python看来, 每个alien都是独立的, 能够独立的修改每个alien.

 前面是把字典存放在列表中, 现在反过来: 将字典存储在字典中.

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chesse']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```

[完整代码](./07/nesting.py)

在字典当中存储字典:

```python
users = {
    'einstein': {
        'gender': 'male',
        'location': 'princton',
    },
    'mcurie': {
        'gender': 'male',
        'location': 'paris',
    },
}
```

## 7. 用户输入和while循环

通过获取用户输入并学会控制程序的运行时间, 可编写出交互式程序.

### 7.1 input()

input()函数让程序暂停运行, 等待用户输入一些文本. 获取用户输入后, Python将其存储在一个变量中, 以方便使用.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

如果提示信息太多或太长, 可以提前定义prompt, 可以考虑三引号模式, 减轻劳动强度.

input()默认返回字符串类型, 如果需要其他类型注意转换.

[input例子](./07/input.py)

数据类型转换函数:
- int()
- float()
- str()

```python
# input()函数返回值为字符串类型, 若需要数值类型需要转换

age = int(input("How old are you? "))

born = 2023 - age
print(f"You was borned in {str(born)}.")
```

### 7.2 while循环

一般情况下, <mark>while循环必须设置程序如何退出</mark>
 
wile循环不断运行, 直到指定的条件不满足为止. 一个典型的while循环:

```python
# 一般 while 循环的三个典型特征
current_number = 1          # 1.循环外初始值
while current_number <= 5:  # 2.恰当的判断条件
    print(current_number)
    current_number += 1     # 3.初始值变化
```

在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为<mark>标志</mark>

```python
...

status = True
while status:
    message = input(prompt)

    if message == "quit":
        status = False
    else:
        print(message)
```

break: 要立即退出while, 不再运行余下的代码, 也不管条件测试的结果如何. break语句用于控制程序流程

```python
...
while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("blabla...")
```

continue: 要返回循环开头, 并根据条件测试结果决定是否继续执行循环

while 的特殊形式: 无判断条件, 使用 continue 和 break 控制程序流程
核心特征: **可以退出!**

while循环用于网络服务端, 需要不间断提供服务, 就没有退出的逻辑要求了, 这是 while 循环的一个特例; 除此之外都需要提供退出机制.

```python
# 打印10以内奇数
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue

    print(num)
```

<mark>break和continue目的是复杂情况下的流程控制, 容易陷入混乱, 尽量少用.</mark>

通过while同列表和字典结合起来使用, 可收集, 存储并组织大量输入, 供以后查看和显示.

[while处理列表示例](./07/while_list.py)

利用while递归删除列表中某一个元素:

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:    # 显然这是一个判断语句, 这也是 python 牛逼所在.
    pets.remove('cat')

print(pets)             # 语句是否在循环体内部要根据实际业务来决定, 根本在于逻辑是否清晰.
```

利用用户输入来填充字典:

```python
responses = {}
polling_active = True

# 信息收集
while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False  # 本质特征是条件判断要有变为False的机制

# 信息回馈
print("\n--- Poll Results ---")
for name, response in reponses.item():
    print(f"{name} would like to climb {response}.")
```

作业: 饭店订单系统雏形

```python
"""
# 第一版: 逻辑错误, 暂时还找不到错误的原因
orders = ['干煸豆角', '鱼香肉丝', '软烧茄子', '辣子鸡块', '鸡蛋豆腐汤']
finished = []

for order in orders:
    order = orders.pop()
    print(f"您的{order}正在制作...")
    finished.append(order)

print("\n您的订单已经完成, 祝您用餐愉快!")
for order in finished:
    print(\torder)
"""
# # 第二版, 运行正常, 但订单反向打印不完美.
# # 试过反转列表, 但是出错!
# orders = ['干煸豆角', '鱼香肉丝', '软烧茄子', '辣子鸡块', '鸡蛋豆腐汤']
# finished = []
#
# while orders:
#     order = orders.pop()
#     print(f"您的{order}正在制作...")
#     finished.append(order)
#
# print("\n您的订单已经完成, 祝您用餐愉快!")
# for fin in finished:
#     print(f"\t{fin}")
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
```

## 8. 函数

函数是被命名的代码块, 用于完成具体的工作, 只有在被调用时才会运行, 调用几次运行几次.
函数存在的意义为代码重用, 即: 

> *凡重复皆可(应)函数*.

### 8.1 定义函数

最简单的函数定义和调用
```python
def greet_user(name):
    """显示简单的问候"""
    print(f"Hello, {name.title()}!")

greet_user("tom")
greet_user("JERRY")
"""
逐行解析:
    1. def 关键字用来定义函数; greet_user()为函数名; 冒号为格式要求.
    2. 所有的缩进构成了函数体; 三引号中的内容称为文档字符串(docstring),Python可以用来生成有关程序中函数的文档.
    3. 函数体内的代码
    4. 空行在形式上表明了函数定义的结束, 虽非强制, 但推荐.
    5. 函数调用, 函数"非调用, 不执行; 调用几次, 执行几次."
"""
```

### 8.2 参数

在上例代码中:
name 称为形参--函数完成期工作所需的一项信息.
"tom"称为实参--调用函数时传递给函数的信息.
位置实参: 多个形参需要传递多个实参, 按照位置顺序传递称为位置实参.
关键字实参: 按照`name="alice"`方式传递实参称为关键字实参, 可忽略顺序.
默认值: 形参给出值称为默认值; 传递实参则按实参运行, 忽略实参则传递默认值.见下例:

```python
def calculator(n, mi=2):
    """简单的幂计算器"""
    return n ** mi

print(calculator(5))
print(calculator(2, 8))

-----------------
25
256
```

### 8.3 返回值

函数一般返回一个或一组值, 以便其他程序调用, 形式: return

一个可选实参:

```python
def full_name(first_name, middle, last):
    """返回简洁的姓名"""
    if middle:
        fullName = first_name + ' ' + middle + ' ' + last
    else:
        fullName = first_name + ' ' + last
    return fullName.title()
```

**注意:** return语句后不应该再有代码, 即使有也不会执行.

函数可返回任何类型的值, 包括列表和字典等较复杂的数据结构.

```python
def buildPerson(first, last):
    """返回一个字典,其中包含有关一个人的信息"""
    person = {'first': first, 'last':last}
    return person
```

### 8.4 函数对复杂数据结构的操作

列表作为实参在函数中的操作:

```python
def print_models(designs, completeds):
    """
    这是一个3D打印公司内部系统的一部分
    模拟打印每个设计, 直到没有为打印的设计为止
    打印每个设计后, 都将其移动到列表completed中
    """
    while designs:
        current = designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current)
        completeds.append(current)

def show_completed(completeds):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed in completeds:
        print("\t" + completed)

designs = ['iphone case', 'robot pendant', 'dodecahedron']
completeds = []

print_models(designs, completeds)
show_completed(completeds)
```

每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个显示打印好的模型;这优于使用一个函数来完成两项工作。编写函数时，如果你发现它执行的任务太多，请尝试将这些代码划分到两个函数中。别忘了，总是可以在一个函
数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。

禁止函数修改列表: `print_models(designs[:], completeds)`, 这样修改的只是列表副本, 原列表不会改动.

### 8.5 传递任意数量的实参

`def function(*argu):`

如果要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后.

`def build_profile(first, last, **user_info):`

形参中的两个星号让Python创建一个名为user_info的空字典, 并将收到的作为键-值对都封装到这个字典中.
> 疑问: 单星号和双星号区别仅仅是数据类型吗?
 
```python
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics'
)

print(user_profile)
```

### 8.6 将函数存储在模块中

函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。 这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

- 导入整个模块: import modle_name
  
  -  使用模块中的函数: module_name.function_name()

- 导入特定的函数: from module_name import function_name
  
  - from module_name import function_1, function_2
  - 直接调用, 不用使用"模块名.函数名"

- 使用as给函数指定别名: from module_name import function_name as fn

- 使用as给模块指定别名: import module_name as mn
  - 调用: `mn.function_name`

- 导入模块中的所有函数: from module_name import * -- 不推荐,容易出错
  - 原因是直接调用函数不用小数点表示法, 如果你不熟悉整个模块很容易造成函数名变量名等等的冲突

一个实例:
[模块代码](./08/pizza.py)
[调用模块的普通代码](./08/making_pizzas.py)


### 8.7 函数编写规范

- 函数名应具有描述性, 且只在其中使用小写字母和下划线

- 包含简要的阐述其功能的注释, 紧跟在函数定义后面, 并采用文档字符串格式

- 形参默认值等号两边不要有空格, `def function_name(par_0, par_1='default value'):`

- 如果模块包含多个函数, 可使用两个空行将相邻的函数分开

- 所有的import语句都应放在文件开头, 唯一的例外是文件开头使用了注释来描述整个程序.

## 9. 类

本章之前的编程都是面向过程的编程, 注重的是解决问题的次序和逻辑, 类比显示世界更像是打工人的思维, 侧重技术细节.
而面向对象编程类比现实世界更像是老板的思维: 达成一个目标需要哪些资源, 以及如何组织这些资源; 整体的思维高度要高了一个维度.
基本概念:
- 类: 更像是设计图, 模版
- 对象: 根据图纸/模版生产出来的实物
- 实例化: 根据类来创建对象称为实例化

### 9.1 创建和使用类

一个简单的示例:
编写一个表示小狗的简单类 Dog --它表示的不是特定的小狗, 而是小狗的模版.
小狗都有名字和年龄
小狗都会蹲下和打滚

```python
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
```

- Dog: 类名. 根据约定, 类首字母大写
- (): 从空白创建的类, 如果括号内有内容, 那么它就是继承自别的类
- 文档字符串docstring: 简要描述类的功能
- 类中的函数称为方法, 有关函数的一切都适用于方法; 变量称为属性
- \_\_init(self)\_\_是一个特殊的方法, 每当根据类创建新实例时, Python都会自动运行它.
    - 前后的双下划线是一种约定, 目的在于避免 Python 默认方法和普通方法发生名称冲突.
- self必不可少, 还必须位于第一个, 是一个指向实例本身的引用, 让实例能够访问类中的属性和方法
- self会自动传递, 创建实例时, 只需要给出后面的实参就可以了.
- 以 self 为前缀的变量可供类中所有方法使用, 我们还可以通过类的任何实例来访问这些变量
- self.name = name获取存储在形参name 中的值, 并将其存储到变量 name 中
- 可通过实例访问的变量称为属性
- 虽然示例代码中小狗能做的有限, 但可以扩展: 如果这个类包含在一个计算机游戏中, 这些方法将包含创建小狗蹲下和打滚的动画效果的代码. 想象一下, 这将极大的简化开发.

根据类创建实例:

```python
# 接上述代码
# 实例化
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

# 调用属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法
your_dog.sit()
my_dog.roll_over()
```

可以看到创建多个实例, 调用属性和方法的方式.

[student代码](./09/student.py)

### 9.2 使用类和实例

可以直接修改实例的属性, 也可以编写方法以特定的方式进行修改

[一个简单的汽车类](./09/car.py)

**修改属性的值**:

- 直接修改属性的值: `my_car.odometer = 56` <mark>有漏洞</mark>, 可以赋值任意数值

- 通过方法修改属性的值:
  
  - ```python
    def update_odometer(self, kiloage):
        """将里程表设置为指定的值"""
        self.odometer = kiloage
    
    ...
    
    my_car.update_odometer(56)
    ```

- 通过方法对属性的值进行递增:
  
  - ```python
    def increment_odometer(self, kilo):
        """将里程表读数增加指定的量"""
        if kilo > 0:
            self.odometer += kilo
        else:
            print("里程表不能倒拨, 请输入大于等于0的数字")
    
    ...
    
    my_car.increment_odometer(100)
    ```

[汽车修改属性值的完整代码](./09/car_2.py)

### 9.3 继承

编写类时, 并非总是要从空白开始. 如果你要编写的类时另一个现成类的特殊版本, 可使用继承. 子类将自动获得父类 (也叫超类) 的所有属性和方法, 同时还可以定义自己的属性和方法.

[简单继承的代码](./09/inherit.py)

子类创建规范:

1. 创建子类时, 父类必须包含在当前文件中, 且位于子类前面

2. 定义子类时, 必须在括号内指定父类的名称: `class ElectricCar(Car):`

3. 方法`__init__()`接受创建实例所需的信息: `def __init__(self, brand, model, year):`

4. super()是一个特殊函数, 帮助Python将父类和子类关联起来, 让子类实例包含父类的所有属性: `super().__init__(brand, model, year)`

5. 增加子类默认属性: `self.battery_size = 70`


*重写父类的方法*:

对于父类的方法, 只要它不符合子类模拟的实物行为, 都可对其进行重写

重写的方法如果与父类方法同名, Python调用方法的优先级子类高于父类

#### 将实例用作属性

使用代码模拟实物时, 会发现自己给类添加的细节越来越多: 属性和方法清单及文件都越来越长. 此时就需要将类的一部分作为独立的类提取出来. 将大型类拆分成多个协同工作的小类.
```python
class Car():
  --snip--

class Battery():
  """一次模拟电动汽车电池的简单尝试"""

  def __init__(self, battery_size=70):
    """初始化电池属性"""
    self.battery_size = battery_size

  def describe_battery(self):
    """打印描述电池容量的消息"""
    print(f"This car has a {battery_size}-kwh battery")


class ElectricCar(Car):
  """电动汽车的独特之处"""

  def __init__(self, brand, model, year):
    """初始化父类的属性, 再初始化电动汽车特有的属性"""
    super().__init__(brand, model, year)
    self.battery = Battery()  ## 特别注意:Buttery()本身为实例, 在此作为属性!!!


my_tesla = ElectricCar('tesla', 'model 3', 2018)

print(my_tesla.get_descriptive_name())

# 这里先调用电动汽车的属性 battery
# 而属性 battery 是由实例 Battery()提供, 从而可以进一步调用实例方法describe_battery()
# "链式反应"! 哈哈哈,有意思.
my_tesla.battery.describe_battery()
```
在上面例子中看似做了很多额外的工作, 但实际情况是现在我们想多详细的描述电池都可以, 且不会导致 ElectricCar 类混乱不堪.
设想一下: 实际工作中(例如游戏)要构建汽车这一复杂的类, 可以将发动机,底盘,变速箱等等系统作为小类,然后再构建 Car()类...
这样代码既清晰又容易维护; 同时程序员的思维也开始分层了, 既关注到细节又能统领全局.

### 9.4 导入类

随着不断地给类添加功能, 文件可能变得很长, 即便你妥善地使用了继承亦如此. 为遵循Python的总体理念, 应让文件尽可能整洁. Python允许你将类存储中模块中, 然后主程序导入所需的模块. 

说人话: 将纯净的类代码存入单独的文件, 然后在主程序中导入, 并且实例化应用; 可以把注意力集中到高层逻辑之上.

[模块代码](./09/carModule.py), [主程序代码](./09/imp.py) 疑问: 如何把模块代码放入统一的目录, 并且还能被主程序调用? "呃...我猜应该是标准库所在的系统目录吧...或者将路径映射到标准库所在目录?"

**注意**: 模块命名要遵循变量命名规则.

导入类的情景:

1. 导入单个类: `from car import Car`

2. 一个模块多个类导入其中之一: `from car import ElectricCar`

3. 从一个模块中导入多个类: `from car import Car, ElectricCar`

4. 导入整个模块: `import car` 使用`module_name.class_name`访问需要的类

5. 导入模块中的所有类: `from module_name import *` 不推荐, 很容易混乱.

6. 在一个模块中导入另一个模块: 父类与子类分成两个模块, 在子类中导入父类`from car import Car`, 然后在实例时按需导入
  - 例如将 Car 放入模块car.py; ElectricCar放入electri_car.py模块
  - 在 electric_car.py 模块中需要: `from car import Car`

一开始应让代码结构尽可能简单, 先尽可能在一个文件中完成所有的工作, 确定一切都能正确运行后, 再将类移到独立的模块中. <mark>先找出让你能够编写出可行代码的方式, 再尝试让代码更为组织有序.</mark>

### 9.5 Python标准库

Python标准库是一组模块, 安装的Python都包含它. 可以使用标准库中的任何函数和类, 为此只需要在程序开头包含一条简单的import语句.

**注意**: 你还可以从其他地方下载外部模块, 一般称为第三方模块.

[标准库练习](./09/dice.py)
忍不住还是晒出来:
```python
# 第一次尝试导入标准库中的模块 random, 其中 randint()返回指定范围内的一个随机整数. 用来模拟骰子的行为
from random import randint


class Dice():
    """模拟掷骰子"""

    def __init__(self, a, b):
        """初始化类属性"""
        self.a = a
        self.b = b

    def play(self):
        """模拟掷骰子游戏"""
        x = int(input(str(self.b) + "面的掷骰子游戏, 你想玩几次? "))
        for _ in range(x):
            print(f"点数: {randint(self.a, self.b)}")


dice = Dice(1, 6)   # 实例化标准样式
dice.play()
Dice(1, 10).play()  # 实例化+调用二合一, 代码更简洁
Dice(1, 20).play()

'''
这段小程序一开始就掉坑里了:
受教材影响, 开始敲代码之前就毫无怀疑的要继承random模块当中的类randint.
百转千回, 耗时几个小时, 才忽然明白: 为什么要继承? 程序需要的不过是一个随机数而已!
至此豁然开朗

教训: 直接聚焦要解决问题的本身, 要以解决问题为导向, 而不是选择哪一条技术路线.
'''
```

### 9.6 类的编码风格

- 类名应采用驼峰命名法, 实例名和方法名都采用小写加下划线命名

- 在每个类定义后面包含一个文档字符串, 简要描述类的功能; 每个模块也都应包含一个文档字符串, 简要描述其中的类或整个模块

- 使用一个空行分隔方法; 两个空行分隔类

- 需要同时导入标准库和自定义的模块时, 先导入标准库, 空行后导入自定义模块.  很容易让人明白模块来自何方. 

原书对面向对象的介绍明显不够, 作为补充请参阅[扩展阅读pythonOOP.md](./09/pythonOOP.md).


## 10. 文件和异常

异常是一种特殊的 Python 类, 用于帮助发生错误时采取相应的措施.
这里的错误当然不包括语法错误和逻辑错误等程序员职责内的工作, 而是面对用户输入等不可控因素造成的错误.

### 10.1从文件中读取数据

文本文件可以存储极大量的信息, 从本章开始将尝试用 Python 来直接读写文件.

先看代码:

```python
with open('../03/wishlist.py') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

"""
代码解析:
- 以任何方式使用文件都必须先打开文件,才能访问它.
- 函数open()只接受一个参数:目标文件名称, 它返回一个表示文件的对象
- 关键字with在访问结束后自动关闭文件
- 关键字as给返回的文件对象取一个别名
- read()在到达文件末尾时返回一个空字符串,所以要使用rstrip()
"""
```

**文件路径**:
Python默认在当前目录下查找文件, 根据操作系统文件组织方式有两种方式指明文件路径,
相对路径和绝对路径. 如果绝对路径比较长可以将其存储在变量中.
实际工作中一般将所需文件存储在程序文件所在目录下的一个子目录中.

**逐行读取**:

```python
filename = '../Python编程从入门到实践.md'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

创建一个包含各行文件内容的列表:

使用关键字 with 时, open()返回的文件对象只在 with 代码块内可用. 如果要在 with 代码块外访问文件的内容, 可以在 with 代码块内将文件存储在一个列表中, 并在 with 代码块外使用该列表. 看代码:

```python
with open('txt/pi.txt') as file:
  lines = file.readlines()

print('lines')  # 确认lines为列表

for line in lines:
  print(line.rstrip())
```

**将文件读取到内存中后, 就可以用任何方式使用/处理这些数据了.**
注意: 读取文本文件时, Python 将其中的所有文本都解读为字符串.如果要使用其中的数字记得数据类型转换.

#### 小结:
- 文件读取代码: `with open('path/filename') as obj:`
- 读取方式有三种:
    1. 一次性读取: `obj.read()`
    2. 逐行读取: `for line in obj:`
    3. 列表读取: `obj.readlines()`

### 10.2 写入文件

示例代码:

```python
file = 'txt/programming.txt'

with open(file, 'w') as file_object:
    file_object.write("I love programming.")
```

- 必须要先建立txt目录, programming.txt可以由程序创建
  - 如果文件已经存在且有内容,w模式将清除所有内容并写入新内容!注意注意!!
- open()实际上有两个实参,第一个是文件名,第二个:
  - 默认'r'--读取模式
  - 'w'--写入模式, 此模式要慎用!!! 如果已有文件内有内容,会被覆盖.
  - 'a'--附加模式     #推测一下: 此模式是否可以由程序创建文件? 居然可以!!!
  - 'r+'--读取和写入模式
- 注意: Python只能将字符串写入文件.数值数据要str()转换

[附加模式写入代码](./10/write.py)
*提示*: 写入模式不会自动添加换行符,需要自己手动添加.

习题[来宾登记](./10/guestList.py)
代码展示
```python
# 来宾签到程序, 并保存姓名到来宾名单中

while True:
    print("Enter 'q' to exit the programm.")
    name = input("Please input your name: ")

    if name == 'q' or name == '':
        break
    else:
        with open('txt/guestList.txt', 'a') as file:
            file.write(name.strip().title() + '\n')
        print(f"Hello, {name.strip().title()}!")
```

### 10.3 异常

程序崩溃让用户看到traceback不好. 不懂技术的用户会被搞糊涂; 懂技术怀有恶意的用户会通过traceback获取你不希望它知道的信息.训练有素的攻击者可根据泄露的信息对你的代码发动攻击.

Python使用try-except代码块处理异常状况, 让程序继续执行不致于崩溃.
例如:

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

显然try部分会发生错误, 那么就会执行except模块而不会崩溃程序继续执行
反之,如果try部分没问题则会正常执行, except模块被忽略.

[完整的try-except-else结构](./10/try.py)

[文件找不到代码](./10/fileNotFind.py)

显然, try-except-else要求知道 Error 类型, 那么总共有多少种 Error 呢?

已知的Error列表:
- ZeroDivisionError
- FileNotFindError

#### 分析文本
split()根据一个字符串创建一个单词列表.
我们可以利用它来分析出一篇文档内有多少个单词(汉语也能计算吗?)
split()以空格为分隔符将字符串拆成多个部分, 并将这些都存储到一个列表中. 所以中文不行.
[文本分析](./10/analyzeText.py)

上面的代码是分析单一文本文件, 那么分析多个文件代码怎么写?
从头再来? No! 忘了函数了吗?
[多文本分析](./10/analyzeTexts.py) 炫一下代码:
```python
# 多文件文本单词数统计

def count_words(file):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file) as obj:
            contents = obj.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        # 计算文件大概包含多少个单词
        words = contents.split()
        print(f"The file {file} has about {len(words)} words.")


files = ['txt/guestList.txt', 'txt/pi.tt', 'txt/programming.txt']
for file in files:
    count_words(file)
```
显然第二个文件不存在, 但程序抛出异常后继续计算第三个文档.

### 10.4 存储数据

一种简单的方式是使用json存储数据.
json.dump()存储数据, json.load()使用数据

```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as obj:
    json.dump(numbers, obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

**重构**
代码能够正确运行, 但可做进一步的改进--将代码划分为一系列完成具体工作的函数. 这样的过程称为重构. 重构让代码更清晰, 更易于理解, 更容易扩展.

[代码实例](./10/Refactor.py)
可以明显的看到重构之后逻辑更为清晰,扩展性更好,但坏处就是代码量大幅增加了
对于小型项目得不偿失, 但对于大型项目, 这点代码量增加的坏处就显得微不足道了.

[未完成的作业](./10/greetUser.py)

## 11. 测试代码
学习使用 Python 模块unittest中的工具来测试代码, 通过测试将使你对自己的代码信心满满.

本章的主要逻辑就是: 自己写的程序不确认是否符合预期, 然后利用语言给出的功能再写一段代码来验证前一段代码的正确性. 至此, 只能是长叹一声.

作为程序员首先应该想清楚逻辑关系再抄起键盘码字, 代码完成之后就应该没啥大问题.
考虑到使用场景, 正常情况+极端状况下多运行几次代码就能消灭 bug
为了验证一段代码要写另一段代码, 谁能保证验证代码的正确性, 难道再写一段吗? 无穷无尽??
所以, 这一章, 以目前的认知来看: 纯属脱裤子放屁!

略过.


至此, 本书的基础部分完结, Part 2实战项目部分打算新开笔记, 所以, 本书第一部分完结撒花.

<mark>END.</mark>2023-12-21
