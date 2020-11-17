import cv2
import matplotlib.pyplot as plt

'直方图均衡化：类似放大方差 把有些图像黑的地方变量一些'
# 1）全局直方图均衡化
src = cv2.imread("../images/28.jpg", 0)

# 全局直方图均值化——这一行代码可进行均值化
dst = cv2.equalizeHist(src)


# 原直方图
hist_src = cv2.calcHist([src], [0], None, [256], [0, 255])  # 这个要使用plt.plot()显示

# 全局均值化后的直方图——方差变大了，可以进行去雾
hist_dst = cv2.calcHist([dst], [0], None, [256], [0, 255]) # 这个要使用plt.plot()显示

# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 结合matplotlib展示多张图片
plt.subplot(221), plt.imshow(src, cmap="gray"), plt.title("Src Image")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dst, cmap="gray"), plt.title("Dst Image")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.plot(hist_src, color='r', label="hist_src"), plt.legend()
plt.subplot(224), plt.plot(hist_dst, color='b', label="hist_dst"), plt.legend()

plt.show()

# 2)CLAHE(限制对比度的自适应直方图均值化)
src = cv2.imread("../images/29.jpg", cv2.IMREAD_GRAYSCALE)

# 1. 全局直方图均衡化
img_equalize = cv2.equalizeHist(src)

# 2. CLAHE自适应均衡化
clahe = cv2.createCLAHE(tileGridSize=(7, 7))    # 在7*7的范围内求均值
img_clahe = clahe.apply(src)

# 原直方图
hist_src = cv2.calcHist([src], [0], None, [256], [0, 255])
# 全局均衡化后的直方图
hist_equalize = cv2.calcHist([img_equalize], [0], None, [256], [0, 255])
# CLAHE均衡化后的直方图
hist_clahe = cv2.calcHist([img_clahe], [0], None, [256], [0, 255])


# 结合matplotlib展示多张图片
# plt.subplot(231), plt.imshow(src, cmap="gray"), plt.title("Src Image")
# plt.xticks([]), plt.yticks([])
# plt.subplot(232), plt.imshow(img_equalize, cmap="gray"), plt.title("Image after Equalzie")
# plt.xticks([]), plt.yticks([])
# plt.subplot(233), plt.imshow(img_clahe, cmap="gray"), plt.title("Image after CLAHE")
# plt.xticks([]), plt.yticks([])
# plt.subplot(234), plt.plot(hist_src, color="b", label="hist_src"), plt.legend()
# plt.subplot(235), plt.plot(hist_equalize, color="g", label="hist_equalize"), plt.legend()
# plt.subplot(236), plt.plot(hist_clahe, color="r", label="hist_clahe"), plt.legend()
# plt.show()

