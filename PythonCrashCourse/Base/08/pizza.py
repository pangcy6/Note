# 第一个模块文件

def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for t in toppings:
        print(f"- {t}")
