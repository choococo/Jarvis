from PIL import Image, ImageFilter, ImageDraw, ImageFont
import matplotlib.pyplot as plt


image = Image.open("./01.jpg")

'加入模糊'
img1 = image.filter(ImageFilter.BLUR)       # 模糊
img2 = image.filter(ImageFilter.DETAIL)     # 增强饱和度
img3 = image.filter(ImageFilter.CONTOUR)    # 轮廓,类似于素描的效果
img4 = image.filter(ImageFilter.EMBOSS)     # 浮雕
# plt.subplot(2, 2, 1)
# plt.imshow(img1)
# plt.subplot(2, 2, 2)
# plt.imshow(img2)
# plt.subplot(2, 2, 3)
# plt.imshow(img3)
# plt.subplot(2, 2, 4)
# plt.imshow(img4)
# plt.axis('off')
# plt.show()
# img3.show()

'ImageDraw的使用'
draw = ImageDraw.Draw(image)        # 创建画板对象，将图片放入其中，这里的画板和plt不同的就是没有界面
draw.point(xy=(200, 300), fill="red")
# plt.imshow(image)
# plt.show()
# image.show()
draw.line(xy=(300, 300, 1000, 1000), fill='blue', width=3)  # 注意画板中的填充是要填完整的颜色名称，不能使用简写
draw.rectangle((30, 50, 80, 100), fill="blue", outline="red", width=4)
draw.rectangle((60, 80, 180, 200), outline="red", width=4)
draw.rectangle((100, 100, 400, 400), outline="red",width=4)
draw.ellipse((100, 100, 400, 400), fill="red", outline="yellow", width=4) # 画椭/圆:矩形左上角，右下角
draw.rectangle((400, 400, 700, 900), outline="red", width=4)
draw.arc((400, 400, 700, 900), start=0, end=270, fill="blue", width=4)     # 画圆弧:矩形左上角，右下角，顺时针
draw.chord((400, 400, 700, 900), start=0, end=180, outline="red", width=4) # 画和弦:矩形左上角，右下角，顺时针

font_path = "../msyh.ttc"
font = ImageFont.truetype(font_path, size=20)
draw.text(xy=(30, 60), text="这是中文字符", fill="red", font=font)
plt.imshow(image)
plt.show()
# image.show()
