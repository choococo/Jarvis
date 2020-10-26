"""
Python 3 中有六的标准的数据类型
    Number
    String
    Dict
    List
    Set
    Tuple
    可变类型和不可变类型
        只有dict和List是可变类型，set比较特殊
        Number,String ,Tuple是不可变类型
    Python中是有自动回收机制的，
    Python中比较优势的是切片和索引的操作，要比Java便捷很多
"""
print("1. Number")
print(1.23e-10)
print(1.23e10)

print(True)
print(True + 1)

print(3 + 4j)
print(type(3 + 4j))         # 打印类型

"""
二进制是以0b开头 0b11=3    bin
八进制是以0o开头 0o11=9    oct
十六进制以0x开头 0x11=17   hex
"""
print(int("0x11", 16))      # 0x11 转换为10进制是多少


print("2. String")
s1 = "hello world, I am a Javis"
print(len(s1))
print(s1[4])
print(s1[2 : 4])            # 取索引从2到4的值，取不到4
print(s1[-1])               # 取到最后一个值
print(s1[::-1])             # 反向索引，可以用于进行逆序
print(s1[:-1])              # 不取最后一个数据
print(s1[:25:1])
print(s1[25:1])             # 这个是取不到值得，从最后一个开始取值，后面没有值
print(s1[-1:1])             # 同上

name = "张三"
name = "李四"
print(name)

# raw 一直转义字符, 一般用在读取文件的时候，文件夹的路径
print("\\")                 # \
print(r"\\")                # \\

print("3. 列表")             # 列表是一个任意类型有序的集合，是一个存放元素的，没有固定的大小




