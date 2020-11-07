import cv2
import time

'图像插值'
img = cv2.imread("../images/1.jpg")
rows, cols, channels = img.shape
print(rows, cols, channels)  # [w, h, c]
time_start = time.time()  # 开始时间

'图片缩放:resize()'
resize1 = cv2.resize(img, dsize=(cols * 2, rows * 2))  # 按尺寸进行缩放
resize2 = cv2.resize(img, dsize=(0, 0), fx=2, fy=2)  # 按比例进行缩放

'几种插值方式'
'1. 双线性插值(默认)'
linear = cv2.resize(img, dsize=(rows * 2, cols * 2), interpolation=cv2.INTER_LINEAR)

'2. 最邻近插值'
nearest = cv2.resize(img, dsize=(cols * 2, rows * 2), interpolation=cv2.INTER_NEAREST)

'3. 基于4x4像素邻域内的三次样条插值'
cubic = cv2.resize(img, dsize=(cols * 2, rows * 2), interpolation=cv2.INTER_CUBIC)

'4. 基于8x8像素邻域内的Lanczos插值'
lanczos = cv2.resize(img, dsize=(cols * 2, rows * 2), interpolation=cv2.INTER_LANCZOS4)

'5. 给予局部像素的重采样'
area = cv2.resize(img, dsize=(cols * 2, rows * 2), interpolation=cv2.INTER_AREA)

cv2.imshow("resize1", resize1)
cv2.imshow("resize2", resize2)
cv2.imshow("linear", linear)
cv2.imshow("nearest", nearest)
cv2.imshow("cubic", cubic)
cv2.imshow("lanczos", lanczos)
cv2.imshow("area", area)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
几种常用插值法的效率是：最近邻插值>双线性插值>双立方插值>Lanczos插值
但是效率和结果成反比,所以根据自己的情况斟酌使用
"""
