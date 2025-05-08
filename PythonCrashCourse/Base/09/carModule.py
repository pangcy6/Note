"""一组用于表示燃油汽车和电动汽车的类"""


class Car():
    """一次模拟汽车的尝试"""

    def __init__(self, brand, model, year):
        """初始化汽车属性"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 3   # 给属性设置默认值的方式

    def get_name(self):
        """返回整洁的描述性信息"""
        long_name = self.brand + " " + self.model + " " + str(self.year)
        # long_name = f"{self.brand} {self.model} {self.year}"
        return long_name

    def get_odometer(self):
        """打印汽车行驶里程"""
        print(f"This car has {self.odometer} kilometers on it.")

    def update_odometer(self, kilo):
        """设置汽车行驶里程"""
        if kilo >= self.odometer:
            self.odometer = kilo
        else:
            print("Odometer callback is prohibited, enter the correct value.")

    def increment_odometer(self, kilo):
        """将里程表增加指定的里程"""
        if kilo >= 0:
            self.odometer += kilo
        else:
            print("Odometer callback is prohibited, enter the correct value.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, brand, model, year):
        """初始化父类属性"""
        super().__init__(brand, model, year)
        self.battery_size = 70

    def battery_info(self):
        print(f"This car has a {self.battery_size} Kwh battery.")
