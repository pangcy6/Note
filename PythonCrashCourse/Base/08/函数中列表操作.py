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
    """显示打印号的所有模型"""
    print("\nThe following models have been printed:")
    for completed in completeds:
        print("\t" + completed)

designs = ['iphone case', 'robot pendant', 'dodecahedron']
completeds = []

print_models(designs, completeds)
show_completed(completeds)
