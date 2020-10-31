import os


def read_txt_to_xyxy_word():
    with open("xyxy.txt", "r") as f:
        strs = f.readlines()
        line = [line.strip("\n") for line in strs]
        # print(line)

    with open("word.txt", "r", encoding="utf8") as f:
        words = [word.strip("\n") for word in f.readlines()]
        # print(words)

    res_list = []
    for xyxy, word in zip(strs, words):
        res = [xyxy.strip("\n"), word]
        res_list.append(res)
    # print(res_list)

    return res_list
#
# a = read_txt_to_xyxy_word()
# print(a[0][0])
# x1, y1, x2, y2  = a[0][0].split(" ")
# print(x1)

# for i in a:
#     # print(i)
#     xyxy = i[0]
#     x1 = int(xyxy.split(" ")[0])
#     y1 = int(xyxy.split(" ")[1])
#     x2 = int(xyxy.split(" ")[2])
#     y2 = int(xyxy.split(" ")[3])
#     word = i[1]
#     print(x1, y1, x2, y2, word)
#     break

import pandas as pd
data = pd.read_table("xyxy.txt",sep=" ",header=None)
words = pd.read_table("word.txt",sep=" ",header=None)
x1,y1,x2,y2 = data.iloc[0,0:4]
word = words.iloc[0]
# print(data)
# print(words)
print(word)
# print(x1,y1,x2,y2)