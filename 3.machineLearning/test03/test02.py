# 深拷贝与浅拷贝
import copy
# a = 1
# b = a
# print(a, b)
# print(id(a), id(b))



li1 = [1, 2, 3]
print(id(li1))
li2 = copy.copy(li1)
print(id(li2))
li1[0] = "hello"
print(li1, li2)

li3 = [[11, 22, 33], [44, 55, 66]]
li4 = copy.copy(li3)
print(id(li3))
print(id(li4))

li3[0][0] = 77
print(li3, li4)

