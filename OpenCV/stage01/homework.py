import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np


input_path = r"../images/1.mp4"
output_path = r"../images/output.mp4"
font = ImageFont.truetype("./msyh.ttc", size=30)
cap = cv2.VideoCapture(input_path)                      # 创建视频对象

# fourcc = cv2.VideoWriter_fourcc(*"XVID")              # 这个格式和下面格式有的在Linux系统中只要一种是好使的
fourcc = cv2.VideoWriter_fourcc(*"DIVX")                # 写入视频常用的格式,为MP4格式
fps = cap.get(cv2.CAP_PROP_FPS)                         # 获取当前视频的帧数
print(fps)

w, h = int(cap.get(3)), int(cap.get(4))                 # 读取视频的宽和高
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h)) # 创建视频写入格式，大小和帧数的对象


while cap.isOpened():
    ret, frame = cap.read()                             # 捕获每一帧图像，ret为每一帧读取的布尔值, frame是每一帧画面
    if ret:                                             # ret == True为有图片可读
        frame = cv2.resize(frame, (w, h))               # 可以对视频大小重新设计尺寸，上面的写入兑现的尺寸也一定要修改
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image)
        draw.rectangle((200, 50, 300, 150), outline="red", width=3)
        draw.text((100, 100), text="中文", fill="red", font=font)

        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # out.write(frame)
        cv2.imshow("", frame)

        if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
