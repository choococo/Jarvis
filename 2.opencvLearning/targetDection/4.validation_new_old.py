import os
import numpy as np
import sys

# box[image_filename, x, y, w, h]
def iou(box1, box2):
    area_box1 = box1[3] * box1[4]
    area_box2 = box2[3] * box2[4]

    x1 = np.maximum(box1[1], box2[1])
    y1 = np.maximum(box1[2], box2[2])
    x2 = np.minimum((box1[1] + box1[3]), (box2[1] + box2[3]))
    y2 = np.minimum((box1[2] + box1[4]), (box2[2] + box2[4]))

    w = np.maximum(0, (x2 - x1))
    h = np.maximum(0, (y2 - y1))
    inter = w * h

    return inter / (area_box1 + area_box2 - inter)


def read_old_txt(path):
    pass


def read_new_txt(path):
    pass


if __name__ == '__main__':
    old_path = r"./label/list_bbox_celeba.txt"
    new_path = r"./label/list_new_bbox.txt"
    j = 0
    with open(old_path,"r") as f:
        old = f.readlines()[2:]
    with open(new_path,"r") as f2:
        new = f2.readlines()
    for i in range(len(old)):
        x1, y1, w1, h1 = map(int, old[i].split()[1:])
        x2, y2, w2, h2 = map(int, new[i].split()[1:])
        box1 = [old[i][0],x1,y1,w1,h1]
        box2 = [new[i][0],x2, y2, w2, h2]
        num = iou(box1,box2)
        if  num < 0.2 :
            j += 1
            # print(old[i].split()[0])
            print(i+1,end=" ")
    print(j)
        # sys.stdout.write("\r >> processing {}/{}".format((i + 1), len(old)))
        # sys.stdout.flush()
    # o(old_path,header=1)
    # new = pd.read_table(new_path,header=None,sep=" ")
    # # print(new.iloc[1:,:])
    # print(old)
    # for i in range(old.shape[0]):

