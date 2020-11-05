import cv2
import numpy as np

'插值算法'
image1 = cv2.imread("../images/1.jpg")
image2 = cv2.imread("../images/8.jpg")

# interpolation - 插值方法。共有5种：
# 1)INTER_NEAREST - 最近邻插值法
# 2)INTER_LINEAR - 双线性插值法（默认）
# 3)INTER_AREA - 基于局部像素的重采样（resampling using pixel area relation）。
# 对于图像抽取（image decimation）来说，这可能是一个更好的方法。
# 但如果是放大图像时，它和最近邻法的效果类似。
# 4)INTER_CUBIC - 基于4x4像素邻域的3次插值法
# 5)INTER_LANCZOS4 - 基于8x8像素邻域的Lanczos插值
# image1 = cv2.resize(image1, (image1.shape[1]*2, image1.shape[0]*2), interpolation=cv2.INTER_LANCZOS4)
image1 = cv2.resize(image1, (image1.shape[1]*2, image1.shape[0]*2), interpolation=cv2.INTER_LINEAR)

print(image1.shape)
print(image2.shape)

cv2.imshow("", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

