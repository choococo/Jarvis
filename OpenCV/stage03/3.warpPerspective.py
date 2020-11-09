import cv2
import numpy as np

'图像透视变换'
# 这里将图像进行透视变换，就是扭曲处理，将不正的图像，变得正
src = cv2.imread("../images/6.jpg")
rows, cols, channels = src.shape

print(rows, cols)

# 1. 获取透视变换矩阵M, getPerspectiveTransform(src, dst)
# src:原图像中四边形定点的坐标
# dst:目标图像中对应的四边形定点的坐标
pst1 = np.array([[25, 30], [180, 25], [10, 190], [190, 190]], dtype=np.float32)
pts2 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])

# 创建一个变换矩阵，将这个矩阵传给放视变换函数cv2.warpPerspective() 就是对图像进行扭曲处理
M = cv2.getPerspectiveTransform(pst1, pts2)

# 进行透视变换
# M:透视变换矩阵
# dsize:指定输出图片的大小
dst = cv2.warpPerspective(src, M, dsize=(rows, cols))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
