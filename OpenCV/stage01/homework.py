import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from stage01 import readtxt

data = readtxt.read_txt_to_xyxy_word()
print(data[0][0])
x1, y1, x2, y2  = data[0][0].split(" ")
word = data[0][1]
print(word)

# data = pd.read_table("xyxy.txt",sep=" ",header=None)
# x1,y1,x2,y2 = data.iloc[0,0:4]
#
# words = pd.read_table("word.txt",sep=" ",header=None)
# word = words.iloc[0, 0]
#
#
input_path = r"../images/1.mp4"
output_path = r"../images/output.mp4"
font = ImageFont.truetype("./msyh.ttc", size=30)
cap = cv2.VideoCapture(input_path)                      # 创建视频对象

fourcc = cv2.VideoWriter_fourcc(*"DIVX")                # 写入视频常用的格式,为MP4格式
fps = cap.get(cv2.CAP_PROP_FPS)                         # 获取当前视频的帧数
frames = cap.get(7)

w, h = int(cap.get(3)), int(cap.get(4))                 # 读取视频的宽和高
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h)) # 创建视频写入格式，大小和帧数的对象
j = 1
i = 0
while cap.isOpened():
    ret, frame = cap.read()                             # 捕获每一帧图像，ret为每一帧读取的布尔值, frame是每一帧画面
    if ret:                                             # ret == True为有图片可读
        frame = cv2.resize(frame, (w, h))               # 可以对视频大小重新设计尺寸，上面的写入兑现的尺寸也一定要修改
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image)
        if i == (int(fps)) * 2:
            print("+++", j)
            x1, y1, x2, y2 = data[j][0].split(" ")
            word = data[j][1]
            j += 1
            i = 0
        draw.text((100, 100 ), text=word, fill="red", font=font)
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), [0, 0, 255], 3)
        i += 1
        cv2.imshow("", frame)
        # out.write(frame)
        if cv2.waitKey(int(fps)) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()