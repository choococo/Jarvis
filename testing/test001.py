# 1. 2000-3200中可以被7整除但是不能被5整除的数
res = []
for i in range(2000, 3201):
    if i % 7==0 and i % 5!=0:
        res.append(i)
print(res)

# 2. 求一个数的阶乘
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(8))

# 3.
def func01(x):
    res = dict()
    for i in range(1, x+1):
        res[i]=i**2
    return res
print(func01(8))

# 4.
str = "34,67,55,33,12,98"
strs = str.split(",")
print(strs)
print(tuple(strs))

# 5.
class Test:
    def __init__(self, x):
        self.x = x
    def getString(self):
        return self.x
    def printString(self):
        print(self.x)

str = "1234"
tt = Test(str)
print(tt.getString())
tt.printString()

# 6.
def func(x, c =50, h=30):
    return int(((2*c*x)/h)**0.5)
print(func(100))

# 7.
def func03(x, y):
    res = [[0 for i in range(y)] for j in range(x)]
    print(res)
    for i in range(x):
        for j in range(y):
            res[i][j]=i*j
    return res
print(func03(3, 5))


# 8.
str = "without,hello,bag,world"
strs = str.split(",")
w = sorted(strs, key=lambda i:i[0])
print(w)
s = ""
for i in range(len(w)):
    s = ",".join(w)
print(s)

# 9.
str = "Practice makes perfect"
print(str.capitalize())
strs = str.split(" ")
print(strs[0].capitalize())
res = []
for i in range(len(strs)):
    w = strs[i].capitalize()
    res.append(w)
print(res)

# w = sorted(strs.upper(), key=lambda i: i[0])
# 10.

str = "hello world and practice makes perfect and hello world again"
strs = str.split(" ")
w = set(strs)
w = sorted(w, key=lambda i:i[0])
b = " ".join(w)
print(b)
# print(strs)



