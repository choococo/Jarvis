import cv2
import numpy as np

img = cv2.imread("../images/6.jpg")
rows, cols, channels = img.shape
a = np.pi / 3
sina = np.sin(a)
print(sina)
cosa = np.cos(a)
scale = 1
M0 = np.float32([[1, 0, 0], [0, 1, 0]])
M1 = np.float32([[1, 0, 0], [0, 1, 0]])
M2 = np.float32([[0.5, 0, 0], [0, 0.5, 0]])  # x轴变为 0.5倍，y 轴变为 0.5倍
# M3 = np.float32([[cosa * scale, sina * scale, -((rows/sina)/2-rows/2)], [-sina * scale, cosa * scale, 0]])  # x轴变为 0.8倍，y 轴变为 0.5倍
M3 = np.float32([[cosa * scale, sina * scale, 0], [-sina * scale, cosa * scale, cols/2]])  # x轴变为 0.8倍，y 轴变为 0.5倍
# M3 = np.float32([[cosa * scale, sina * scale, -((rows/sina)/2-rows/2)], [-sina * scale, cosa * scale, 0]])  # x轴变为 0.8倍，y 轴变为 0.5倍
M = cv2.getRotationMatrix2D(center=(cols // 2, rows // 2), angle=60, scale=1)

dst = cv2.warpAffine(img, M, dsize=(rows, cols))  # API旋转45度效果
dst0 = cv2.warpAffine(img, M0, dsize=(rows, cols))  # API旋转45度效果
dst1 = cv2.warpAffine(img, M1, dsize=(rows, cols))  # 正常效果
dst2 = cv2.warpAffine(img, M2, dsize=(rows, cols))  # 缩小的效果0.5
dst3 = cv2.warpAffine(img, M3, dsize=(rows, cols))

cv2.imshow("dst", dst)
cv2.imshow("dst0", dst0)
# cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
