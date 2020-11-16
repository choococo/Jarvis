import os

with open("./label/list_new_bbox.txt", "w") as f:
    for i in range(10):
        strs = ['1', '2', '3']
        strs = " ".join(strs)
        f.writelines(strs)
        f.flush()
        f.write("\n")
