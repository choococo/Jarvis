import cv2
import numpy as np


'使用numpy创建数组，也可以放入到opencv中，opencv可以显示成图片'
print(bin(255))
print(int(0b11111111))

img = np.zeros([400, 400, 3])
img = np.ones([400, 400, 3])
img = np.arange(400* 400 * 3).reshape([400, 400, 3]) / (400 * 400 * 3)  # 渐变色, 数据在0-1时，不需要加uint8
img = np.uint8(np.arange(400* 400 * 3).reshape([400, 400, 3]) / (400 * 400 * 3) * 255)  # 这里需要加uint8，无符号整形

print(np.max(img), np.min(img), np.mean(img))
img = np.random.rand(400, 400, 3)                                       # 0-1之间的数
img = np.random.randn(400, 400, 3)
img = np.random.normal(0, 10, (400, 400 ,3))

'uint8是无符号，表示8个位，用来存放图像像素'
img = np.zeros([400, 400, 3], np.uint8)

img[..., 2] = 255                                                       # 红色
print(img)
print(img.shape)

cv2.imshow("", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit(0)
cv2.destroyAllWindows()
# cv2.imwrite("01.jpg", img)