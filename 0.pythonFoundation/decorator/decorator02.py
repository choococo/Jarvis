"""
装饰器的使用：
    ·先定义一个装饰器（帽子）
    ·再定义你的业务函数或者类（人）
    ·最后把这装饰器（帽子）扣在这个函数（人）头上
"""

instances = {}


# 类装饰器
def logger(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print("Train object has initing...")
        if not cls_name in instances:
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        print("Train object has inited.")
        return instances[cls_name]

    return get_instance


# 方法装饰器
def logger2(func):
    def wrapper(*args, **kwargs):
        print("Train is begining...")
        func(*args, **kwargs)
        print("Train has finished.")

    return wrapper


@logger
class Train:

    def __init__(self):
        print("init")

    @logger2
    def __call__(self):
        print("training")


train = Train()
train()
