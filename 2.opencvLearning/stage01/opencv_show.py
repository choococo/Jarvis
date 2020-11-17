import cv2
import numpy as np
from PIL import Image, ImageFilter

cap = cv2.VideoCapture("../images/1.mp4")                               # 打开视频
fps = cap.get(cv2.CAP_PROP_FPS)                                         # 查看当前视频的fps
print(fps)
w, h = int(cap.get(3)), int(cap.get(4))                                 # 获取当前视频的宽和高
print(w, h)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # 转换成Image对象，需要注意BGR2RGB
        frame = frame.filter(ImageFilter.CONTOUR)                       # 轮廓，相当于素描
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    else:
        break
    if cv2.waitKey(int(1000 // fps // 2)) & 0xFF == ord('q'):
        break
    cv2.imshow("中文".encode("gbk").decode(errors="ignore"), frame)
    # cv2.waitKey(0)
cap.release()                                                           # 关闭视频
cv2.destroyAllWindows()                                                 # 关闭所有窗口
