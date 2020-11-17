import os


"""
批量给文件重命名
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
"""
path = r"E:\4. 个人\1. 个人学习\1. AI\personal\学习视频"

try:

    for root, dirs, files in os.walk(path):
        # print(root,"->", files)

        # 遍历文件
        for i, file in enumerate(files):
            i = str(i)
            print(i)
            # print(os.path.join(root, file))
            filename_all = os.path.join(root, file)
            index = filename_all.rindex("\\")
            path_re = filename_all[:index+1]
            str_split = filename_all[index+1:]
            # print(path_re, "->", str_split)
            origin_name = filename_all
            path_final = ''.join(i)+'.ts'
            save_path = os.path.join(path_re, path_final)
            print(filename_all,"->",save_path)
            os.rename(filename_all, save_path)
        print("_________________")
        # 遍历所有文件夹
        # for dir in dirs:
        #     print(os.path.join(root, dir))
except:
    raise Exception("error")

