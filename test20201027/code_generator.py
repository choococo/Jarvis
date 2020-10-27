#
#  @Author : choococo
#  @Time : 20201027

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import sys
import random
import os


class CodeGenerator:

    def __init__(self, width=240, height=60, save_path=None, numbers=None, font=None, font_size=40):
        """
        默认构造器, 初始化参数
        :param width: 图片的宽
        :param height: 图片的高
        :param save_path: 图片的保存路径
        :param numbers: 需要生成的图片
        :param font: 字体
        """
        self._width = width
        self._height = height
        self._save_path = save_path
        self._numbers = numbers
        self._font = font
        self._font_size = font_size

    def _randBgColor(self):
        """
        生辰随机背景颜色
        :return: Image的背景图像
        """
        return (random.randint(32, 127),
                random.randint(32, 127),
                random.randint(32, 127))

    def _randCodeColor(self):
        """
        随机生成验证码颜色
        :return: 验证码的RGB颜色的元组
        """
        return (random.randint(65, 255),
                random.randint(65, 255),
                random.randint(65, 255))

    def _randRote(self, image, alpha=None):         # 但是这里目前没有用到，可能需要进行切片得到每一个，旋转后再paste回去
        """
        随机旋转图片
        :param alpha: 旋转角度
        :param image: 需要旋转的图片
        :return: 旋转后的单个验证码
        """
        return image.roate(np.random.randint(0, 90))

    def _imageFilter(self, image):
        """
        给验证码加入滤波
        :param image: 需要加入滤波的图片
        :return: 加入滤波的Image对象
        """
        return image.filter(ImageFilter.GaussianBlur)

    def _randLinexyxy(self):
        """
        生成随机的干扰线的坐标x1,y1,x2,y2
        :return: 两个坐标组合成的元组
        """
        x1 = random.randint(5, 20)
        y1 = random.randint(5, 20)
        x2 = random.randint(190, 230)
        y2 = random.randint(190, 230)
        xyxy = [x1, y1, x2, y2]
        return xyxy

    def _randArcDegree(self):
        """
        弧线的随机角度
        :return: 返回随机角度
        """
        return np.random.randint(0, 180)

    def _randColorLine(self):
        """
        随机选择干扰线中的填充颜色
        :return: 颜色的字符串str
        """
        return np.random.choice(["red", "blue", "yellow", "gray", "black", "white"])

    def _imageAddRandLine(self, image, numbers=2):
        """
        给图片加入随机的干扰直线或者曲线
        :param draw: 需要加入的画板对象上的图片，这样可以方便画直线和曲线
        :param numbers: 加入干扰线的条数，默认为2条干扰线
        :return: 加入干扰直线或曲线的Image对象
        """
        draw = ImageDraw.Draw(image)
        color1 = self._randColorLine()
        color2 = self._randColorLine()

        for i in range(numbers):
            draw.line(xy=self._randLinexyxy(), fill=color1, width=2)
            draw.arc(xy=self._randLinexyxy(), start=self._randArcDegree(), end=self._randArcDegree(), fill=color2, width=1)
        return image

    def _img_new(self):
        """
        创造一张空白的图片，作为验证码图片的底
        :return: Image的对象
        """
        return Image.new("RGB", (self._width, self._height), color=(0, 0, 0))
        # return Image.new("RGB",(240,60),(0,0,0))

    def _randChar(self):
        """
        生成随机的英文+数字
        :return: 生成的英文和字符
        """
        a = chr(random.randint(65, 90))
        b = chr(random.randint(97, 122))
        # c = str(random.randint(0, 9))
        c = chr(random.randint(48, 57))
        return random.choice([a, b, c])

    def _generateBg(self, choice=0):
        """
        直接利用numpy生成均匀分布，然后转换成图片，即为背景
        :param choice: 0为第一种创建方式，1位第二种创建方式
        :return: 验证码的背景图
        """
        if choice == 0:
            return Image.fromarray(np.uint8(np.random.uniform(0, 255, size=(60, 240, 3))))
        elif choice == 1:
            image = self._img_new()
            draw = ImageDraw.Draw(image)
            # 手动填充像素
            for i in range(self._width):
                for j in range(self._height):
                    draw.point(xy=(i, j), fill=(self._randBgColor()))
            return image
        else:
            raise Exception("没有其他创建背景的方式，请选择choice=0或者choice=1")

    def _addCaptcher(self, image):
        """
        填充验证码
        :param image: 背景图片Image 对象
        :return: 添加好验证码的Image对象
        """
        draw = ImageDraw.Draw(image)
        x_list = [0]
        for i in range(4):
            # ???????????这里面还要加入字符的漂移，让两个字符重叠的情况不允许超过一半，要写判断放入字符
            # 对xy坐标重新使用
            # if x_list is None:
            #     x_list.append(0)
            x = 10 + np.random.randint(1/2 * x_list[i], 60)
            x_list.append(x)
            y = np.random.randint(0, self._height - self._font_size)
            draw.text((x, y),self._randChar(),font=self._font,fill=self._randCodeColor())
            # draw.text((60*i+10,10),self._randChar(),font=self._font,fill=self._randCodeColor())
        return image

    def generator(self, numbers=1):
        """
        验证码生成器，只要这一个方法对外开放
        :param numbers: 需要生成验证码图像的数量，默认为一张
        :return: 按理说应该为空，只需要保存即可
        """
        for i in range(numbers):
            img = self._generateBg(choice=np.random.choice([1]))
            img = self._addCaptcher(image=img)
            img = self._imageAddRandLine(img)
            # img = self._imageFilter(img)
            # img.show()
            # img.save(self._save_path + "{}.jpg".format((i + 1)))
            img.save(os.path.join(self._save_path, "{}.jpg".format((i + 1))))
            sys.stdout.write("\r >>processing {}/{}".format((i + 1), numbers))
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
        sys.stdout.write("生成完成")


if __name__ == '__main__':
    save_path = r"./pic"                                                        # 保存路径
    font_size = 40
    font = ImageFont.truetype(font="msyh.ttc", size=40)                         # 字体
    code_gen = CodeGenerator(save_path=save_path, numbers=None, font=font)      # 实例化
    code_gen.generator(10)                                                      # 调用生成器



