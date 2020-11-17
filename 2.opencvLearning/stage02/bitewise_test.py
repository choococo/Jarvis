import cv2
import numpy as np
from PIL import Image


'图像的运算'
image1 = cv2.imread("../images/1.jpg")
image2 = cv2.imread("../images/7.jpg")

# 形状要一样
image_or = cv2.bitwise_or(image1, image2)           # 进行或运算，求并集，加法
print(image_or.shape)

image3 = np.uint8((image1 * 0.7 + image2 * 0.3))    # 这两张图片进行了融合，但是颜色的色差不是两张原图的内容

image_and = cv2.bitwise_and(image1, image2)         # 与运算，求空集，取反色_有0则0，全1则1
print(image1[0, 0, 0])                              # 126
print(image2[0, 0, 0])                              # 0
print(image_and[0, 0, 0])                           # 0

# cv2.bitwise(src, dst) 只需要输入第一个参数即可，第二个参数是进行返回，一般可以不需要
image_not = cv2.bitwise_not(image1)                 # 取反，0就是1,1就是0
print(image_not[0, 0, 0])

image_xor = cv2.bitwise_xor(image1, image2)         # 异或，相同为0，不同为1
print(image_xor[0, 0 , 0])


# cv2.imshow("", image1)
# cv2.imshow("", image_or)
# cv2.imshow("", image_and)
# cv2.imshow("", image_not)
cv2.imshow("", image_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()


