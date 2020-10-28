from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class PILUsing:

    def __init__(self, path):
        pass

    def show_Image_Size(self, image):
        """
        查看图片的大小
        :param image: 图片
        :return: 返回图片的w和h的元组
        """
        return image.size


if __name__ == '__main__':
    path = r"./01.jpg"
    img = Image.open(path)  # 使图片处于可读的模式，这里的操作和文件的操作是一样的，是文件处于一个可读的模式
    # print(img)              # 输出图片的对象的信息，相当于Java中的toString()的内容
    # img.show()            # 这里展示的图片不会被压缩

    ' 查看图像的尺寸'
    w, h = img.size
    # print((w, h))           # (1800, 1200)
    # plt.imshow(img)         # 把图片放到plt中显示，这里图片会被压缩
    # plt.show()              # 利用plt显示图片

    '图像转换numpy'
    # a = np.array(img)       # 转换成numpy数组的形式
    # print(a.shape)          # 查看array的形状，这里就是图片的原始whc的形状
    # print(a.size)           # 计算的个数

    'numpy数组转换成图像'
    # image = Image.fromarray(a)  # 从数组中转换为Image对象
    # print(image)                # 输出图像的信息，只不过，这里面的信息经过上面的转换之后有所丢失
    # image.show()                # 展示图片

    '返回像素直方图，统计每个像素值出现的次数'
    # his = img.histogram()       # 返回像素直方图
    # print(his)                  # 打印出现的像素值的次数
    # print(len(his))             # 输出使用的像素值的个数
    # plt.hist(his)               # 放入到plt中进行条形图的统计
    # plt.show()                  # 显示

    '查看指定坐标位置的像素点的RGB值，返回的是一个元组'
    # pixes = img.getpixel((120, 80)) # 得到固定位置的像素值元组
    # print(pixes)                    # 输出

    '使用切片的方法裁剪图片'
    # print(np.array(img)[100:600, 500:1000, :])  # HWC 进行切片
    # img2 = Image.fromarray(np.array(img)[100:600, 500:1000, :])
    # # img2.show()
    # plt.imshow(img2)
    # # plt.xticks([])                # 隐藏x坐标轴
    # # plt.yticks([])                # 隐藏y坐标轴
    # plt.axis('off')                 # 隐藏坐标轴，与上面的用法是一样的
    # plt.show()

    '使用Image中裁剪工具裁剪图片'
    # img2 = img.crop((400, 500, 1000, 1000))
    # # img2.show()
    # plt.imshow(img2)
    # plt.show()

    '按指定大小缩放图片'
    # x = img.resize((100, 100))
    # x = img.resize((int(w / 2), int(h / 2)))    # 注意这里面必须是整数
    # # x.show()
    # plt.imshow(x)
    # plt.show()

    'thumbnail 按最大边等比例缩放，没有返回值'
    # img.thumbnail((1000, 800))
    # plt.imshow(img)
    # plt.show()

    '将一张图片按指定位置粘贴到另一张图片上'
    img02 = Image.open("02.jpg")
    img.paste(img02, (10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    '保存图片'
    img.save("03.jpg")

    '生成一张空白图片'
    image = Image.new("RGB", (100, 100), (0, 0, 0))
    image.show()


