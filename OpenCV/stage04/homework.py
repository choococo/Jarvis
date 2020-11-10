import cv2
import numpy as np
import matplotlib.pyplot as plt

'OTSU二值化__二值化就是0和1的值'
image = cv2.imread("../images/1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # 将彩色图转换成灰度图

# 将灰度图转化为二值图(0, 255), otsu是自动求取阈值 -- no
# 阈值二值化：小于阈值thresh(ret)的取0，小于阈值的取maxval
ret, binary = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 阈值反二值化：小于阈值取maxval，大于阈值取0
ret, binary_inv = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# 阈值截断
# 小于阈值，为原始值值，大于阈值的为阈值 - no
ret, truncate = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
# 阈值取零
# 小于阈值，为0; 大于阈值为原始值 - no
ret, tozero = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_TOZERO | cv2.THRESH_OTSU)
# 阈值反取零
# 小于阈值，为原始值; 大于阈值为零
print(gray[gray < 113])
ret, tozero_inv = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_TOZERO_INV | cv2.THRESH_OTSU)
print(tozero_inv[gray < 113])

x, y, w, h = cv2.boundingRect(binary_inv)
# x, y, w, h = cv2.boundingRect(binary)
img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(ret)  # 自动求阈值，不用手动定
cv2.imshow("", binary)
cv2.imshow("1", binary_inv)
cv2.imshow("img", img)
# cv2.imshow("", truncate)
# cv2.imshow("", tozero)
# cv2.imshow("", tozero_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
