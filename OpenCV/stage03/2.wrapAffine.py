import cv2
import numpy

'图像仿射变换'
img = cv2.imread("../images/6.jpg")
rows, cols, channels = img.shape

# 1.创建仿射变换矩阵
# 1）平移
M0 = numpy.float32([[1, 0, 0], [0, 1, 0]])
# 1）平移
M1 = numpy.float32([[1, 0, 20], [0, 1, 80]])  # 沿x轴平移+20，沿y轴平移+80
# M1 = numpy.float32([[1, 0, 20], [0, 1, 80]])  # 沿x轴平移+20，沿y轴平移+80
# 2）缩放
M2 = numpy.float32([[0.8, 0, 0], [0, 0.5, 0]])  # x轴变为0.8倍，y轴变为0.5倍
# 3）旋转：调用getRotationMatrix2D()获取仿射矩阵

# center是旋转的中心点；
# angle是旋转角度(正数表示逆时针)，如angle = 15
# 表示逆时针旋转15度；
# scale标量是缩放因子，0.5
# 表示缩小，2
# 表示放大一倍，-2
# 表示放大一倍后再做(上下 + 左右)
# 翻转。
# M30 = numpy.float32([[1, 0, 0], [0, 1, 0]])#
M30 = numpy.float32([[numpy.sqrt(3)/2, 0.5, 0], [-0.5, numpy.sqrt(3)/2, 0]])#
# M3 = cv2.getRotationMatrix2D(center=(0,0), angle=0, scale=0.5)
# M3 = cv2.getRotationMatrix2D((cols//2, rows//2), 45, scale=0.8)  # angle=45表示逆时针旋转45度。scale=0.5表示缩小到原来的一半。
M3 = cv2.getRotationMatrix2D((cols//2, rows//2), 45, scale=0.5)  # angle=45表示逆时针旋转45度。scale=0.5表示缩小到原来的一半。
# 4）倾斜
M4 = numpy.float32([[1, 0.5, 0], [0, 1, 0]])# 沿x轴倾斜0.5倍
M5 = numpy.float32([[1, 0, 0], [0.5, 1, 0]])# 沿y轴倾斜0.5倍
# 5）翻转/镜像
# M6 = numpy.float32([[-1, 0, cols], [0, 1, 0]])  # 绕y转翻转，沿x轴平移cols个像素单位
M6 = numpy.float32([[1, 0, 0], [0, -1, rows]])  # 绕x转翻转，沿y轴平移rows个像素单位
M7 = numpy.float32([[-1, 0, cols], [0, -1, rows]])  # 绕y转翻转、绕x转翻转，最后沿x轴平移cols个像素单位、沿y轴平移rows个像素单位

# 2.进行仿射变换
# M: 仿射变换矩阵
# dsize: 指定输出图片的大小
dst0 = cv2.warpAffine(img, M0, dsize=(cols, rows))  # 平移
dst1 = cv2.warpAffine(img, M1, dsize=(cols, rows))  # 平移
dst2 = cv2.warpAffine(img, M2, dsize=(cols, rows))  # 缩放
dst30 = cv2.warpAffine(img, M30, dsize=(cols, rows))  # 旋转
dst3 = cv2.warpAffine(img, M3, dsize=(cols, rows))  # 旋转
dst4 = cv2.warpAffine(img, M4, dsize=(cols * 2, rows * 2))  # 倾斜
dst5 = cv2.warpAffine(img, M5, dsize=(cols * 2, rows * 2))  # 倾斜
dst6 = cv2.warpAffine(img, M6, dsize=(cols, rows))  # 翻转/镜像
dst7 = cv2.warpAffine(img, M7, dsize=(cols, rows))  # 翻转/镜像




# cv2.imshow("img pic", img)
# cv2.imshow("dst1 pic", dst0)
# cv2.imshow("dst1 pic", dst1)
# cv2.imshow("dst2 pic", dst2)
# cv2.imshow("dst3 pic", dst30)
# cv2.imshow("dst3 pic", dst3)
# cv2.imshow("dst4 pic", dst4)
# cv2.imshow("dst5 pic", dst5)
# cv2.imshow("dst6 pic", dst6)
cv2.imshow("dst7 pic", dst7)
cv2.waitKey(0)
cv2.destroyAllWindows()