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


# import pandas as pd
# data = pd.read_table("xyxy.txt",sep=" ",header=None)
# words = pd.read_table("word.txt",sep=" ",header=None)
# x1,y1,x2,y2 = data.iloc[0,0:4]
# word = words.iloc[0]
# # print(data)
# # print(words)
# print(word)
# # print(x1,y1,x2,y2)