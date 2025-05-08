# 面向对象编程第一次尝试

# 定义类
class Student():
    """第一次模拟学生的简单尝试"""

    def __init__(self, name, gender, age):
        """属性初始化"""
        self.name = name
        self.gender = gender
        self.age = age

    def read(self):
        """模拟学生读书"""
        print(f"{self.name.title()} is reading now.")

    def write(self):
        """模拟学生写字"""
        print(f"{self.name.title()} is writing in classroom.")

    def talk(self):
        """模拟学生自我介绍"""
#         msg = f"Hi, My name is {self.name.title()}.\n\
# I'm {self.age} years old.\n\
# I'd love basketball.\n\
# Btw, I'm {self.gender}."
        # 三引号重写:
        msg = f"""Hi, My name is {self.name.title()}.
I'm {self.age} years old.
I'd love basketball.
Btw, I'm {self.gender}."""
        # 总结: 三引号和普通引号除了对分行的处理不同外, 其他一切相同.
        # 为了保持打印输出格式, 这个代码格式还真有点丑.
        print(msg)


# 实例化
num1 = Student("bob", "male", 18)
num2 = Student("alice", "female", 16)

print(num1.name.title())
num1.read()
num2.talk()
num1.write()
num1.talk()
