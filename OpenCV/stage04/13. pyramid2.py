import cv2
import numpy as np

'利用苹果和橘子创建一个新的水果——就是将一半的苹果和一半的橘子拼在一起，然后模糊'
'知道之后感觉很low+无趣'

# 图像无缝融合：使用图像金字塔创建一个新的水果，'Orapple'
A = cv2.imread("../images/14.jpg")
B = cv2.imread("../images/15.jpg")
print(A.shape)  # (256, 256, 3)
print(B.shape)  # (256, 256, 3)

# 1）高斯金字塔
GA = A.copy()
gpA = [GA]
for i in range(6):
    GA = cv2.pyrDown(GA)
    gpA.append(GA)
# print(np.shape(gpA))
print(len(gpA))

GB = B.copy()
gpB = [GB]
for i in range(6):
    GB = cv2.pyrDown(GB)
    gpB.append(GB)
print(np.shape(gpB))

# 2）拉普拉斯金字塔
lpA = [gpA[6]]
print(np.shape(lpA))
# 从小到大一张张上采样到原图大小
for i in range(6, 0, -1):
    print(i)
    GE = cv2.pyrUp(gpA[i])
    # 下采样-上采样=轮廓
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)
# print(lpA)
exit(0)
lpB = [gpB[6]]
for i in range(6, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# 3）拼接苹果和橘子
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, channels = la.shape
    ls = np.hstack((la[:, 0:cols // 2, :], lb[:, cols // 2:, :]))
    # ls = numpy.vstack((la[:, :cols // 2], lb[:, cols // 2:]))
    LS.append(ls)
# cv2.imshow("",LS[6])
ls_ = LS[0]
print(np.shape(ls_))
for i in range(1, len(LS)):
    # 使用最低频率的进行上采样，和拼接的轮廓融合缝隙
    ls_ = cv2.pyrUp(ls_)
    # cv2.imshow("",ls_)
    ls_ = cv2.add(ls_, LS[i])
cv2.imshow(f"xxx{i}", ls_)

# 直接合成的图片
rows, cols, channels = A.shape
real = np.hstack((A[:, 0:cols // 2, :], B[:, cols // 2:, :]))
cv2.imshow("real", real)

cv2.waitKey(0)
cv2.destroyAllWindows()
