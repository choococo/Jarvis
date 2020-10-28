import numpy as np

'索引和切片'
'索引会降维，切片不会'
x = np.arange(24).reshape([2,3,4])
print(x)
print(x[0])
print(x[0:1])
print(x[:1])
print(x[1:])
print(x[:,1:2,:1])
print(x[0][1][0],x[1][1][0])
print(x[0,1,0],x[1,1,0])

print(x[0][1][2])                                     # 取完当前轴之后，再这个基础上继续取

print(x[0,1,2])                                       # 按照轴的顺序连续取值
print(x[1:2,1:])
print(x[:2,1:])
print(x[1:,1])
print(x[:,1:])
print(x[:,:3,:3])

a = np.array([1,2,3,4,5,6])
print(np.array([a[0],a[2],a[4]]))
print(np.array([1,3,5]))
print(a[[0,2,4]])

a = np.array([[3,5,9],[4,2,1],[6,3,7]])                 # 9, 2, 7
print(a[[2,0,1],[1,2,0]])                               # [第0轴的索引，第1轴的索引]
print(a[[0,1,2],[2,1,2]])                               # [第0轴的索引，第1轴的索引]
# [3,9,4]


print(a[:1,:1],a[:1,2:],a[1:2,:1])
print(np.array([a[0,0],a[0,2],a[1,0]]))
# #
a = np.array([[8,5,9],[4,2,1],[6,3,7]])
print(a[[[2,0],[1,1]],[[1,2],[0,2]]])                   # [[第0轴的索引]，[第1轴的索引]]
# [[3,9], [4,1]].


a = np.arange(12).reshape([3,2,2])
# print(a)
print(a[:,:,:1])                                        # 取得第一列
print(a[...,:1])                                        # 取得第一列
print(a[...,1:])                                        # 取得第一列以后的列
#
x = np.arange(12).reshape([3,2,2])
print(x)
print(x[:2,1:2,:1])#[[[2]],[[6]]]


'小数操作'
a = np.floor(3.5)                                       # 向下取整
b = np.ceil(3.5)                                        # 向上取整
c = np.int(3.6)                                         # 强转
d = np.pi                                               # PI
e = np.round(d,3)                                       # 四舍五入
f = np.around(d,3)                                      # 四舍五入
g1 = np.rint(3.4)
g2 = np.rint(3.5)
h1, h2 = np.modf(3.5)                                   # 分割成小数和整数
print(f)
print(g1, g2)
print(h1, h2)

a = np.arange(1, 10)
# b = np.split(a ,3)                                      # 平均分割数组
c, d, e, f = np.split(a,[3,5,8])                          # 按照指定元素的位置分割数组
print(c, d, e, f)