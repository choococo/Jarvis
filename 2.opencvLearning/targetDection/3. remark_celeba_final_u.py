import cv2
import os
import sys
import time

"""
@Auth : choococo lzy
重新标注CelebA数据集，利用opencv的xml 自动化重标注——perfect
"""


class RemarkCelebA:
    def __init__(self, old_label_txt, new_label_txt, image_dir, face_xml_path):
        """
        初始化
        :param old_label_txt: 旧的标签文本
        :param new_label_txt: 新的标签文本
        :param image_dir: 图像路径
        :param face_xml_path: 人脸检测xml
        """
        self._old_label_txt = old_label_txt
        self._new_label_txt = new_label_txt
        self._image_dir = image_dir
        self._face_xml_path = face_xml_path

    def _read_old_label_txt(self, old_label_txt, index):
        """
        读取旧的标签文本信息
        :param old_label_txt: 旧的标签文本
        :param index: 图片的索引
        :return: 图片的filename x y w h
        """
        with open(old_label_txt, 'r') as f:
            labels = [line.strip("\n") for line in f.readlines()][2:]
            data = labels[index]
            return data.split()

    def _length_old_label_txt(self, old_label_txt):
        """
        返回旧的标签文本包含图片的数量
        :param old_label_txt: 旧的标签文本
        :return: 图片的数量
        """
        with open(old_label_txt, 'r') as f:
            return [line.strip("\n") for line in f.readlines()][0]

    def _length_new_label_txt(self):
        with open(self._new_label_txt) as f:
            length = len(f.readlines())
        return length

    def _show_img(self, faces, image, index, isShow=False):
        """
        显示图片
        :param faces: 人脸的坐标的二维数组
        :param image: 正在检测的图片
        :param index: 图片的索引
        :param isShow: 是否显示
        :return: 显示图片
        """
        if isShow == True:
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h + 10), (255, 0, 0), 2)

                cv2.imshow(f"{index}", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            return

    def celeba_remark(self, interval=10, isShow=False):
        """
        重新标注celeba数据
        :param interval: 每个interval张图片显示一次
        :param isShow: 是否显示图片
        :return: 进度条
        """
        # before_len = self._length_new_label_txt()
        before_len = 0
        face_cascade = cv2.CascadeClassifier(self._face_xml_path)
        # length = self._length_old_label_txt(self._old_label_txt)
        length = 46
        with open(self._new_label_txt, "a+") as f:
            # 遍历图片
            for i, img_name in enumerate(os.listdir(self._image_dir)):
                # if i < before_len:
                #     continue
                # 打开图片
                image = cv2.imread(os.path.join(self._image_dir, img_name))
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(3, 3))
                # 判断人脸的个数是否>1
                if len(faces) >= 1:
                    x, y, w, h = faces[0]
                    x, y, w, h = str(x), str(y), str(w), str(h)
                    # 将img_name x y w h 按照空格的方式写入新的标签文本
                    f.write("{} {} {} {} {}".format(img_name, x, y, w, h))
                    # strs = " ".join([img_name, x, y, w, h])
                    # f.writelines(strs)
                    f.write("\n")
                    f.flush()
                # elif len(faces) == 0:
                #     # 读取旧的当前图片的标签
                #     filename, x, y, w, h = self._read_old_label_txt(self._old_label_txt, i)
                #     # 写入到文件中
                #     strs = " ".join([filename, x, y, w, h])
                #     f.writelines(strs)
                #     f.write("\n")
                #     f.flush()
                # 隔n张图片显示一次
                # if i % interval == 0:
                #     self._show_img(faces, image, i, isShow=isShow)
                sys.stdout.write("\r >> processing {}/{}".format((i + 1), length))
                sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.flush()
            sys.stdout.write("标签重生成完成！")


if __name__ == '__main__':
    t1 = time.time()
    face_xml_path = r"./haarcascades/haarcascade_frontalface_alt.xml"  # 人脸检测
    old_label_txt = r"./label/list_bbox_celeba.txt"  # 旧的框标签txt文件
    new_label_txt = r"./label/list_new_bbox1.txt"  # 重新生成的框的标签txt文件
    image_dir = r"./images"  # 需要重新标注的图片的路径
    # image_dir = r"F:\BaiduNetdiskDownload\img_celeba\img_celeba"  # 需要重新标注的图片的路径
    remark_celeba = RemarkCelebA(old_label_txt, new_label_txt, image_dir, face_xml_path)
    remark_celeba.celeba_remark(interval=1, isShow=True)
    print(time.time() - t1)

    # 【注意】每一次中断后，（1）手动添加一行空的CRLF
