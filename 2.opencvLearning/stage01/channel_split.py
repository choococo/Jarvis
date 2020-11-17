import cv2
import numpy as np
from PIL import Image


'opencv中通道C的格式是：BGR，PIL中通道的格式是RGB'
img = cv2.imread("../images/1.jpg")                             # 读取图片
# print(img.shape)

'通道分离的方式一：'                                              # 索引赋值
b = img[:, :, 0:1]
g = img[:, :, 1:2]
r = img[:, :, 2:]
# img_new = np.concatenate([r, g, b], axis=2)                   # cat融合


'通道分离的方式二：'
b, g, r = cv2.split(img)
img_new = cv2.merge([r, g, b])
print(b.shape)                                                  # 注意这里通道分离后，只有宽和高两个维度
print(g.shape)
print(r.shape)

'通道分离的方式三：'
zeros = np.zeros([img.shape[0], img.shape[1]], dtype=np.uint8)  # 注意这里要加上uint8
print(zeros.shape)
img_b = cv2.merge([b, zeros, zeros])                            # 注意这种合并的方式, 实现通道分离显示
img_g = cv2.merge([zeros, g, zeros])                            # 注意这种合并的方式, 实现通道分离显示
img_r = cv2.merge([zeros, zeros, r])                            # 注意这种合并的方式, 实现通道分离显示
print(img_b.shape)

'通道分离的方式四：分别进行赋值'
img_new[..., 0] = 0
img_new[..., 1] = 0
img_new[..., 2] = 0

# cv2.imshow("0", img_new)
cv2.imshow("0", img_new)
if cv2.waitKey(0) & 0xFF == ord("q"):
    exit(0)
cv2.destroyAllWindows()


