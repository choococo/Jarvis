import os
from PIL import Image


img_path = r"../pic02"              # 图片存放路径
save_path = r"../pic03"             # 保存路径
"""
将图片按照最长边进行等比例缩放，得到一张固定大小的图片，如果不能填充整张图片，使用像素填充
"""
def square_img(img_path, save_path):
    if not os.path.exists(save_path):               # 处理过后的图片的保存路劲
        os.mkdir(save_path)
    for i, name in enumerate(os.listdir(img_path)):
        filename = os.path.join(img_path, name)    # 新的路径
        img = Image.open(filename)
        img.thumbnail((224, 224))                   # 按照最长边进行等比缩放
        w, h = img.size
        print(w, h)
        bg_img = Image.new("RGB", (224, 224), (0, 0, 0))
        if w == 224:
            bg_img.paste(img, (0, int((224 - h) / 2)))
        elif h == 224:
            bg_img .paste(img, (int((224 - w) / 2), 0))
        else:
            bg_img.paste(img, (int((224 - w) / 2), int(224 - h / 2)))
        bg_img.show()
        bg_img.save(os.path.join(save_path, "{}.jpg".format(str(i))))
square_img(img_path, save_path)


