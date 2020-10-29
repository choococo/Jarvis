from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

'图像扭曲'
def randBgColor():
    """
    生辰随机背景颜色
    :return: Image的背景图像
    """
    return (random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127))

img_bg = Image.new("RGB", (240, 60))
image = Image.new("RGB", (40, 40))

draw = ImageDraw.Draw(img_bg)
# 手动填充像素
for i in range(240):
    for j in range(60):
        draw.point(xy=(i, j), fill=randBgColor())

# img_bg.show()

font = ImageFont.truetype(font="msyh.ttc", size=30)
draw2 = ImageDraw.Draw(image)
for i in range(40):
    for j in range(40):
        draw2.point(xy=(i, j), fill=randBgColor())
draw2.text(xy=(8, 1), text="C", font=font, fill='red')
image = image.rotate(30)

image = np.array(image)
print(image[0][0]) # (40, 40, 3)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # print("--", image[i][j])
        if image[i][j][0] == 0 and image[i][j][1] == 0 and image[i][j][2] == 0:
            image[i][j][0], image[i][j][1], image[i][j][2] = randBgColor()[0], randBgColor()[1], randBgColor()[2]
image = Image.fromarray(image)

# image.show()

for i in range(4):
    img_bg.paste(image, (10 + 60 *i, 10))
img_bg.show()

'网上找的图像变形，没有试验成功，好累'
import numpy as np
p=np.array([[0,0.],[0,1],[1,1],[1,0]])
q=np.array([[0.3,0.3],[0,1],[1,1],[1,0]])
import matplotlib.image as py
from PIL import Image


p=np.array([[0,0.],[0,1],[1,1],[1,0]])
q=np.array([[0.3,0.3],[0,1],[1,1],[1,0]])
# img=py.imread(r'D:\PycharmProject\test20201027\pil/02.jpg')
img = Image.open("1.png")
img = np.array(img)
u,v=img.shape[:2]
def f(i,j):
    return i+0.1*np.sin(2*np.pi*j)
def g(i,j):
    return j+0.1*np.sin(3*np.pi*i)
M=[]
N=[]
for i in range(u):
    for j in range(v):
        i0=i/u
        j0=j/v
        u0=int(f(i0,j0)*512)
        v0=int(g(i0,j0)*512)
        M.append(u0)
        N.append(v0)
m1,m2=max(M),max(N)
n1,n2=min(M),min(N)
r=np.zeros((m1-n1,m2-n2,3))
for i in range(u):
    for j in range(v):
        i0=i/u
        j0=j/v
        u0=int(f(i0,j0)*512)-n1-1
        v0=int(g(i0,j0)*512)-n2-1
        r[u0,v0]=img[i,j]
img = Image.fromarray(img)
img.show()
img.save('./2.png')
