import random

"猜数字"
while True:
    str = input("请输入一个数字：")
    print(str)
    if str.isdigit():
        print(str)
    else:
        raise Exception("输入不为数字，请重新输入")

