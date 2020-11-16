import cv2
import os
import sys

"""
重新标注CelebA数据集，利用opencv的xml
"""
old_label_txt = r"./label/list_bbox_celeba.txt"
new_label_txt = r"./label/list_new_bbox.txt"
image_dir = r"./images"


def read_old_label_txt(old_label_txt, index):
    """
    加载旧的框标签数据信息，作为字典方便查找opencv中框不到的数据
    :param old_label_txt: 旧的标签文件
    :param index: 需要查找的图片的所有信息的索引
    :return: 返回旧的标签数据的filename, x, y, w, h
    """
    with open(old_label_txt, 'r') as f:
        labels = [line.strip("\n") for line in f.readlines()][2:]
        data = labels[index]
        filename, x, y, w, h = data.split()
        # print(filename, x, y, w, h)
        return data.split()


def length_old_label_txt(old_label_txt):
    with open(old_label_txt, 'r') as f:
        return [line.strip("\n") for line in f.readlines()][0]


# filename, x, y, w, h = read_old_label_txt(old_label_txt, 2)

face_xml_path = r"./haarcascades/haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(face_xml_path)

with open(new_label_txt, "w") as f:
    length = length_old_label_txt(old_label_txt)
    # 遍历图片
    for i, img_name in enumerate(os.listdir(image_dir)):
        # print(i)
        # filename, x, y, w, h = read_old_label_txt(old_label_txt, i)
        # print(img_name)
        # 打开图片
        image = cv2.imread(os.path.join(image_dir, img_name))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(3, 3))

        # print("发现{0}个人脸".format(len(faces)))
        # 判断人脸的个数是否>1
        if len(faces) >= 1:
            x, y, w, h = faces[0]
            x, y, w, h = str(x), str(y), str(w), str(h)
            # 将img_name x y w h 按照空格的方式写入新的标签文本
            strs = [img_name, x, y, w, h]
            strs = " ".join(strs)
            f.writelines(strs)
            f.write("\n")
        elif len(faces) == 0:
            # 读取旧的当前图片的标签
            filename, x, y, w, h = read_old_label_txt(old_label_txt, i)
            # 写入到文件中
            strs = [filename, x, y, w, h]
            strs = " ".join(strs)
            f.writelines(strs)
            f.write("\n")
        # 隔一段时间显示一次
        # if i % 1 == 0:
        #     for (x, y, w, h) in faces:
        #         cv2.rectangle(image, (x, y), (x + w, y + h + 10), (255, 0, 0), 2)
        #         # roi_face = gray[y:y + h, x:x + w]
        #         # roi_color = image[y:y + h, x:x + w]
        #         cv2.imshow("image", image)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        sys.stdout.write("\r >> processing {}/{}".format((i + 1), length))
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("标签重生成完成！")
    # break
