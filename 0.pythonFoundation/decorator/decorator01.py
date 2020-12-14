"""
装饰器的使用：
    ·先定义一个装饰器（帽子）
    ·再定义你的业务函数或者类（人）
    ·最后把这装饰器（帽子）扣在这个函数（人）头上
"""


# 定义装饰器
def decorator(func): # 装饰器
    def wrapper(*args, **kwargs): # wrapper: 包装
        return func()
    return wrapper # 返回包装对象


# 定义业务函数，并进行装饰
@decorator
def function():
    print("hello, decorator")