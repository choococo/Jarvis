import cv2
import numpy as np

'cv2打开的图像就是numpy形式的——cv2和numpy是合起来使用的'


'画直线、圆、椭圆、矩形、多边形'
img = cv2.imread("../images/1.jpg")                                         # 读取图片
pts = np.array([[100, 100],[200, 150],[300, 150],[300, 300], [100,150]])
cv2.line(img, (100, 100), (300, 300), (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
cv2.circle(img, (100, 100), 100, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.polylines(img, [pts], color=(0, 0, 255), thickness=3, isClosed=0)
cv2.imshow("图片".encode("gbk").decode(errors="ignore"), img)                # 显示图片，这种会丢失字符，感觉不好
if cv2.waitKey(0) & 0xFF == ord("q"):
    exit(0)
cv2.destroyAllWindows()
