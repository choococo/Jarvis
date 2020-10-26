print("python 中交换两个值")
a = 3
b = 4

print("方法1")
z = a
a = b
b = z
print(a, b)

print("方法2")
a = 3
b = 4
a = a + b
b = a - b
a = a - b
print(a, b)

print("方法3")
a = 3
b = 4
a, b = b, a
print(a, b)

print("方法4")
a = a ^ b           # a=7
b = a ^ b           # b=3  b=a^b^b=a
a = a ^ b
print(a, b)