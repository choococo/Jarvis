old_label_txt = r"./label/list_bbox_celeba.txt"
new_label_txt = r"./label/list_new_bbox.txt"
image_dir = r"./images"

import numpy as np
import pandas as pd

txt = pd.read_table(new_label_txt)


# txt = np.loadtxt(new_label_txt)
print(txt)

# def read_old_label_txt(old_label_txt, index):
#     """
#     加载旧的框标签数据信息，作为字典方便查找opencv中框不到的数据
#     :param old_label_txt: 旧的标签文件
#     :param index: 需要查找的图片的所有信息的索引
#     :return: 返回旧的标签数据的filename, x, y, w, h
#     """
#     with open(old_label_txt, 'r') as f:
#         labels = [line.strip("\n") for line in f.readlines()]
#         length = labels[0]
#         print(length)
#         data = labels[2:][index]
#         filename, x, y, w, h = data.split()
#         print(filename, x, y, w, h)
#         return data.split()
#
# def length_old_label_txt(old_label_txt):
#     with open(old_label_txt, 'r') as f:
#         return [line.strip("\n") for line in f.readlines()][0]
#
#
# filename, x, y, w, h = read_old_label_txt(old_label_txt, 0)
# print(length_old_label_txt(old_label_txt))