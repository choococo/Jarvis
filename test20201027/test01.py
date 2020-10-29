from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

'单个验证码图片旋转测试Demo'


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

image.show()
image.save("1.png")

# for i in range(4):
#     img_bg.paste(image, (10 + 60 *i, 10))
# img_bg.show()