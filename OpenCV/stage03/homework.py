import cv2
import numpy as np

img = cv2.imread("../images/6.jpg")             # 这里为结果好看，要保证图像为正方形，即w=h
rows, cols, channels = img.shape
print(rows, cols)
"""
旋转矩阵
        _             _
    M = |cosa  -sina 0|
        |sina  cosa  0|
        -             -
    允许在任意地方进行旋转，需要进行如下修改
    |alpha  beta  (1-alpha)*center_x-beta*center_y|
    |-beta  alpha beta*center_x+(1-alpha)*center_x|
    alpha=scale*cosa  beta=scale*sina
    
"""
center_x = rows // 2
center_y = cols // 2
scale = 0.7
a = np.pi / 4
alpha = scale * np.sin(a)
beta = scale * np.cos(a)
M0 = np.float32([[1, 0, 0],
                 [0, 1, 0]])
M1 = np.float32([[alpha, beta, (1 - alpha) * center_x - beta * center_y],
                 [-beta, alpha, beta * center_x + (1 - alpha) * center_y]])
print((1 - alpha) * center_x - beta * center_y)
print(-center_x - cols)
M2 = cv2.getRotationMatrix2D((center_x, center_y), 45, scale=scale)


dst0 = cv2.warpAffine(img, M0, dsize=(rows, cols))
dst1 = cv2.warpAffine(img, M1, dsize=(rows, cols))
dst2 = cv2.warpAffine(img, M2, dsize=(rows, cols))


# cv2.imshow("dst0", dst0)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
