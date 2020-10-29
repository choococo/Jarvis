from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

'单个验证码图片旋转测试Demo_加入交叉'
def randBgColor():
    """
    生辰随机背景颜色
    :return: Image的背景图像
    """
    return (random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127))

img_bg = Image.new("RGB", (240, 60))
image = Image.new("RGB", (60, 60))

draw = ImageDraw.Draw(img_bg)
# 手动填充像素
for i in range(240):
    for j in range(60):
        draw.point(xy=(i, j), fill=randBgColor())

# img_bg.show()

font = ImageFont.truetype(font="msyh.ttc", size=40)
draw2 = ImageDraw.Draw(image)
for i in range(40):
    for j in range(40):
        draw2.point(xy=(i, j), fill=randBgColor())
draw2.text(xy=(20, 0), text="5", font=font, fill=(255, 0, 0))
image = image.rotate(30)

image = np.array(image)
# print(image[0][0]) # (40, 40, 3)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # print("--", image[i][j])
        if image[i][j][0] == 0 and image[i][j][1] == 0 and image[i][j][2] == 0:
            image[i][j][0], image[i][j][1], image[i][j][2] = randBgColor()[0], randBgColor()[1], randBgColor()[2]

point = np.zeros(shape=(60, 240, 3))
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # print("--", image[i][j])
        if image[i][j][0] == 255 and image[i][j][1] == 0 and image[i][j][2] == 0:
        # if image[i][j].any([255, 0, 0]):
            point[i+10][j+10] = np.array([255, 0,0])


print(point)
# print(point.shape)
point_new = point
print(point_new[..., 0] == 255)
mask = point_new[..., 0] == 255
print("-----", point[mask].shape)
# print(point_new)


# point_by_color = image[]
# mask = image[:, :] == [255, 0, 0]
# idxs = np.where(image[:, :] == [255, 0, 0])
# print(idxs[0].shape)
# print(image[idxs].shape)
# res= np.stack(idxs, axis=1)
# print(res.shape)
# print(res + np.array([10, 10, 0]))
# for w, h, c in zip(idxs[0], idxs[1], idxs[2]):
#     print([w, h, c])
#     res.append([w, h, c])

image = Image.fromarray(image)

# image.show()
# image.save("1.png")
img_bg.paste(image, (10, 10))
img_bg.paste(image, (19,10))
img_bg = np.array(img_bg)
print(img_bg.shape)

print(img_bg[mask].shape)
img_bg[mask] = (255,0,0)
print(img_bg.shape)
img_bg = Image.fromarray(img_bg)
# for i in range(4):
#     img_bg.paste(image, (10 + 60 *i, 10))
img_bg.show()

