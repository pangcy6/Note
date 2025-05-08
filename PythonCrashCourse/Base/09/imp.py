# 从模块文件carModule.py中导入一个类
# from carModule import Car
# 从一个模块中导入多个类
from carModule import Car, ElectricCar

my_audi = Car('Audi', 'RS4', 2023)
print(my_audi.get_name())
tesla = ElectricCar('Tesla', 'Module S', 2022)
tesla.battery_info()

'''
导入整个模块的写法: import carModule
实例化写法: audi = carModule.Car('Audi', 'RS4', 2022)
    tesla = carModule.ElectricCar('Tesla', 'Module 3', 2023)
调用方法写法: print(tesla.battery_info())
**仅在实例化时的写法有差异.**

原因也简单: 你导入的是整个模块, 就要明确的指出实例化模块当中的哪个类;
如果仅仅是简单的指明类名, 那么这个类来自哪里就有歧义了.
'''
