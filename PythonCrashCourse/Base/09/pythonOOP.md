# 搞懂 Python 面向对象编程

[参考地址](https://pythondjango.cn/python/advanced/1-python-object-class-programming/)
Author: 大江狗
Date: 2023-12-19
---

## 类(Class)与对象(Object)
类(Class)是用来描述具有相同属性(Attribute)和方法(Method)对象的集合。对象(Object)是类(Class)的具体实例。比如每个学生都有名字和分数，这是他们共同的属性。这时我们就可以设计一个学生类, 用于记录学生的名字和分数，并自定义方法打印出他们的名字和方法。

- 属性(Attribute): 类里面用于描述所有对象共同特征的变量或数据。比如学生的名字和分数。
- 方法(Method): 类里面的函数，用来区别类外面的函数, 用来实现某些功能。比如打印出学生的名字和分数。

要创建一个类我们需要使用关键词class. 这个学生类Student看上去应该是这样的:

```python
# 创建一个学生类
class Student:
    # 定义学生属性，初始化方法
    def __init__(self, name, score):  # 被称为构造函数, 实例化时自动执行.
        self.name = name
        self.score = score

    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))
```

在这个案例中，我们只定义了一个抽象的类，电脑并没有创建什么存储空间。只有当我们完成类的实例化(Instance)时，电脑才会创建一个具体的对象（Object），并为之分配存储空间。所以对象（Object)是类（Class)的一个实例。

要创建一个具体的学生对象(Object)，我们还需要输入:

```python
student1 = Student("John", 100)
student2 = Student("Lucy", 99)
```

在这个案例中，Student是类，student1和student2是我们创建的具体的学生对象。当我们~~输入~~执行到上述代码时，Python会自动调用默认的__init__初始构造函数来生成具体的对象。关键字self是个非常重要的参数，代表创建的对象本身。

当你创建具体的对象后，你可以直接通过student1.name和student1.score来分别获取学生的名字和分数，也可以通过student1.show()来直接打印学生的名字和分数。

## 类变量(class variables)与实例变量（instance variables）

假设我们需要在Student类里增加一个计数器number，每当一个新的学生对象(Object)被创建时，这个计数器就自动加1。由于这个计数器不属于某个具体学生，而属于Student类的，所以被称为类变量(class variables)。而姓名和分数属于每个学生对象的，所以属于实例变量(instance variables)，也被称为对象变量(object variables)。

这个新Student类看上去应该是这样的:

```python
# 创建一个学生类
class Student:
    # number属于类变量，定义在方法外，不属于具体实例
    number = 0
    # 定义学生属性，初始化方法
    # name和score属于实例变量，定义在方法里
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 此处有错误
        number = number + 1

    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))
```

类变量和实例变量的区别很大，访问方式也也不一样。

- 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。访问或调用类变量的正确方式是类名.变量名或者self.__class__.变量名。self.__class__自动返回每个对象的类名。
- 实例变量：定义在方法中的变量，属于某个具体的对象。访问或调用实例变量的正确方式是对象名.变量名或者self.变量名.

注意到上述Student类有个错误没? 我们试图直接使用number = number + 1调用属于类的变量number。正确的方式是使用Student.number或self.__class__.number访问属于类的变量。下面的代码才是正确的:

```python
# 创建一个学生类
class Student:
    # number属于类变量，不属于某个具体的学生实例
    number = 0
    
    # 定义学生属性，初始化方法
    # name和score属于实例变量
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1
    
    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))

# 实例化，创建对象
student1 = Student("John", 100)
student2 = Student("Lucy", 99)

print(Student.number)  # 打印2
print(student1.__class__.number) # 打印2
```

## 类方法(Class method)

正如同有些变量只属于类，有些方法也只属于类，不属于具体的对象。你有没有注意到属于对象的方法里面都有一个self参数, 比如__init__(self), show(self)? self是指对象本身。属于类的方法不使用self参数， 而使用参数cls，代表类本身。另外习惯上对类方法我们会加上@classmethod的修饰符做说明。

同样拿Student为例子，我们不用print函数打印出已创建学生对象的数量，而是自定义一个类方法来打印，我们可以这么做:

```python
class Student:

    # number属于类变量，不属于某个具体的学生实例
    number = 0    # 类属性定义方式
    
    # 定义学生属性，初始化方法
    # name和score属于实例变量
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1   # 类属性调用方式
    
    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))
    
    # 定义类方法，打印学生的数量
    @classmethod
    def total(cls):   # 类方法定义
        print("Total: {0}".format(cls.number))


# 实例化，创建对象
student1 = Student("John", 100)
student2 = Student("Lucy", 99)

Student.total()  # 打印 Total: 2 类方法的调用
"""
小结: 类属性和类方法不属于任何对象
定义:
    类属性: 位于类内部置顶, 同时处于函数体外
    类方法: 都有一个 cls 参数, 同时上一行带有@classmethod修饰符
    顺便提一句: 对象方法都带有一个self参数
调用:
    类属性: className.name
    类方法: className.methodName()
"""
```

## 类的私有属性(private attribute)和私有方法(private method)

类里面的私有属性和私有方法以双下划线__开头。私有属性或方法不能在类的外部被使用或直接访问。我们同样看看学生类这个例子，把分数score变为私有属性，看看会发生什么。

```python
# 创建一个学生类
class Student:

    # 定义学生属性，初始化方法
    # name和score属于实例变量, 其中__score属于私有变量
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.__score))

# 实例化，创建对象
student1 = Student("John", 100)

student1.show()  # 打印 Name: John, Score: 100
student1.__score  # 打印出错，该属性不能从外部访问。

# 私有属性只能通过方法间接使用, 不能直接调用那就更不可能从外部更改
# 这是否可以类比其他语言的封装呢? 对! 没错, 就是封装!
# 至于私有属性也是仅可以在类内部相互访问, 外部禁止.
# 这样就极大的提高了程序的安全性, 同时利用此特性可以实现某些微妙的功能.
```

如果你将score变成__score, 你将不能直接通过student1.__score获取该学生的分数。show()可以正常显示分数，是因为它是类里面的函数，可以访问私有变量。

私有方法是同样的道理。当我们把show()变成，__show()你将不能再通过student1.__show()打印出学生的名字和分数。值得注意的是私有方法必需含有self这个参数，且把它作为第一个参数。

在面向对象的编程中,通常情况下很少让外部类直接访问类内部的属性和方法，而是向外部类提供一些按钮,对其内部的成员相互进行访问,以保证程序的安全性，这就是封装。

## @property的用法与神奇之处

在上述案例中用户不能用student1.__score方式访问学生分数，然而用户也就知道了__score是个私有变量。我们有没有一种方法让用户通过student1.score来访问学生分数而继续保持__score私有变量的属性呢？这时我们就可以借助python的@property装饰器了。我们可以先定义一个方法score(), 然后利用@property把这个函数伪装成属性。见下面例子:

```python
# 创建一个学生类
class Student:

    # 定义学生属性，初始化方法
    # name和score属于实例变量, 其中score属于私有变量
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    # 利用property装饰器把函数伪装成属性
    @property
    def score(self):
        print("Name: {}. Score: {}".format(self.name, self.__score))

# 实例化，创建对象

student1 = Student("John", 100)

student1.score  # 打印 Name: John. Score: 100

"""
小结:
    私有属性用于类内部使用, 不可从外部直接访问, 只能通过方法间接访问
    私有方法仅能在类内部使用, 外部不可使用, 非用不可只能通过其他方法间接使用
    私有属性可通过@property装饰器定义一个方法, 利用@property把方法伪造成属性, 外部普通属性方式调用
    疑问: 这样设计的意义何在? 估计是严谨性和灵活性共存吧.
"""
```

注意： 一旦给函数加上一个装饰器@property,调用函数的时候不用加括号就可以直接调用函数了

## 类的继承(Inheritance)

面向对象的编程带来的最大好处之一就是代码的重用，实现这种重用的方法之一是通过继承(Inheritance)。你可以先定义一个基类(Base class)或父类(Parent class)，再按通过class 子类名（父类名)来创建子类(Child class)。这样子类就可以从父类那里获得其已有的属性与方法，这种现象叫做类的继承。

我们再看另一个例子，老师和学生同属学校成员，都有姓名和年龄的属性，然而老师有工资这个专有属性，学生有分数这个专有属性。这时我们就可以定义1一个学校成员父类，2个子类。

```python
# 创建父类学校成员SchoolMember
class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def tell(self):
        # 打印个人信息
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


# 创建子类老师 Teacher
class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age) # 利用父类进行初始化/可写成super().__init__(self, name, age) 
        self.salary = salary
    
    # 方法重写
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))


# 创建子类学生Student
class Student(SchoolMember):

    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
    
    def tell(self):
        SchoolMember.tell(self)
        print('score: {}'.format(self.score))


teacher1 = Teacher("John", 44, "$60000")
student1 = Student("Mary", 12, 99)

teacher1.tell()  # 打印 Name:"John" Age:"44" Salary: $60000
student1.tell()  # Name:"Mary" Age:"12" score: 99
```

上述代码中，你注意到以下几点了吗？

在创建子类的过程中，你需要手动调用父类的构造函数__init__来完成子类的构造。
在子类中调用父类的方法时，需要加上父类的类名前缀，且需要带上self参数变量。比如SchoolMember.tell(self), 这个可以通过使用super关键词简化代码。
如果子类调用了某个方法(如tell())或属性，Python会先在子类中找，如果找到了会直接调用。如果找不到才会去父类找。这为方法重写带来了便利。

实际Python编程过程中，一个子类可以继承多个父类，原理是一样的。第一步总是要手动调用__init__构造函数。

## super()关键字调用父类方法

在子类当中可以通过使用super关键字来直接调用父类的中相应的方法，简化代码。在下面例子中，学生子类调用了父类的tell()方法。super().tell()等同于SchoolMember.tell(self)。当你使用Python super()关键字调用父类方法时时，注意去掉括号里self这个参数。

```python
# 创建子类学生Student
class Student(SchoolMember):

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
    
    def tell(self):
        super().tell() # 等同于 SchoolMember.tell(self)
        print('score: {}'.format(self.score))
```

## 静态变量(static variable)和静态方法(static method)

静态变量和静态方法都属于类的静态成员，它们与普通的实例变量和实例方法不同，静态变量和静态方法只属于定义它们的类，而不属于某一个实例对象。

由于Python属于动态语言，不存在绝对的静态变量，所以类变量(比如下例中的number)一般就是静态变量，无需显示地声明。把类中的方法声明为静态方法，可以使用@staticmethod装饰器，如下例中的func1方法

```python
# 创建一个学生类
class Student:
    # number属于类变量，定义在方法外，不属于具体实例
    number = 0
    # 定义学生属性，初始化方法
    # name和score属于实例变量，定义在方法里
    def __init__(self, name, score):
        self.name = name
        self.score = score
       
        Student.number = number + 1
        
    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))
    
    # 静态方法无法使用cls和self参数访问类或实例的变量
    @staticmethod
    def func1():
        print("this is static function!")
```

静态变量和静态方法都可以通过类名和实例对象进行访问, 同时不像类方法和实例方法，静态方法无法接收cls和self作为第一个参数。

<mark>总结</mark>
1. 类属性和类方法不属于任何对象
    - 定义:
        - 类属性: 位于类内部置顶, 同时处于函数体外
        - 类方法: 都有一个 cls 参数, 同时上一行带有@classmethod修饰符
        - 顺便提一句: 对象方法都带有一个self参数
    - 调用:
     - 类属性: className.name
     - 类方法: className.methodName()

2. 私有属性和私有方法
    - 私有属性用于类内部使用, 不可从外部直接访问, 只能通过方法间接访问
    - 私有方法仅能在类内部使用, 外部不可使用, 非用不可只能通过其他方法间接使用
    - 私有属性可通过@property装饰器定义一个方法, 利用@property把方法伪造成属性, 外部普通属性方式调用
    - 疑问: 这样设计的意义何在? 估计是严谨性和灵活性共存吧.
