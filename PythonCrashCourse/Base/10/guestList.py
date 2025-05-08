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
