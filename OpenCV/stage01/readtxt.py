import os

with open("xyxy.txt", "r") as f:
    strs = f.readlines()
    line = [line.strip("\n") for line in strs]
    print(line)

with open("word.txt","r", encoding="utf8") as f:
    words = [word.strip("\n") for word in f.readlines()]
    print(words)

for xyxy, word in zip(strs, words):
    res = [xyxy.strip("\n"), word]
    print(res)