import cv2
import matplotlib.pyplot as plt

# 1. 将图片转化为灰度图
img = cv2.imread("../images/18.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 对于比较暗的地方进行高亮处理
abs = cv2.convertScaleAbs(gray, alpha=6, beta=0)
abs = cv2.GaussianBlur(abs, ksize=(5, 5), sigmaX=0)
ret, thresh = cv2.threshold(abs, 15, 255, cv2.THRESH_BINARY)
# 形态学操作(去除中间的黑色噪点)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(11, 19))
close = cv2.morphologyEx(abs, cv2.MORPH_CLOSE, kernel)  # 闭操作：先膨胀再腐蚀
open = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel)

# 3. 加入高斯平滑
# gaussian = cv2.GaussianBlur(open, (5, 5), sigmaX=0)

# 4. Canny算法
canny = cv2.Canny(image=open, threshold1=50, threshold2=150)

# cv2.imshow("gray", gray)
# cv2.imshow("abs", abs)
# cv2.imshow("close", close)
# # cv2.imshow("gaussian", gaussian)
# cv2.imshow("canny", canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
imags = [img, gray, abs, close, open, canny]
titles = ["Input Image", "Gray", "ABS", "Close", "open", "Canny"]
plt.figure(figsize=(10, 10))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(imags[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
