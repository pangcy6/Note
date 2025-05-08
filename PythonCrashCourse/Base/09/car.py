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


my_car = Car('BMW', '320i', 2018)
print(my_car.get_name())
my_car.get_odometer()
my_car.odometer = 1008      # 可以自由调整里程表是一个不合理的选择, 如何进行限制?
my_car.get_odometer()
my_car.model = "M340i"
print(my_car.get_name())
