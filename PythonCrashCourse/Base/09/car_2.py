class Car():
    """一次模拟汽车的尝试"""

    def __init__(self, brand, model, year):
        """初始化汽车属性"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 3  # 给属性设置默认值的方式

    def get_name(self):
        """返回整洁的描述性信息"""
        # long_name = self.brand + " " + self.model + " " + str(self.year)
        long_name = f"{self.brand} {self.model} {self.year}"
        return long_name

    def get_odometer(self):
        """打印汽车行驶里程"""
        print(f"This car has {self.odometer} kilometers on it.")

    def update_odometer(self, kilo):
        """设置汽车行驶里程"""
        if kilo >= self.odometer:
            self.odometer = kilo
        else:
            print("Odometer callback is prohibited, please enter the correct value.")

    def increment_odometer(self, kilo):
        """将里程表增加指定的里程"""
        if kilo >= 0:
            self.odometer += kilo
        else:
            print("Odometer callback is prohibited, please enter the correct value.")


# 实例化
my_car = Car('BMW', '320i', 2018)
print(my_car.get_name())  # 调用方法并进行处理
my_car.get_odometer()		# 纯调用方法

# 直接修改属性的值, 这里有**漏洞**, 可以任意修改数值.封装可以解决吗?
my_car.odometer = -88
my_car.get_odometer()

# 通过方法修改属性的值
my_car.update_odometer(230)
my_car.get_odometer()

# 通过方法对属性的值进行递增
my_car.increment_odometer(100)
my_car.get_odometer()
