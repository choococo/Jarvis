import cv2
import matplotlib.pyplot as plt

'直方图反向投影'
# 感兴趣区域
roi = cv2.imread("../images/30.jpg")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 目标图像
target = cv2.imread("../images/16.jpg")
hsv_target = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# 1)统计ROI的直方图 下面参数的含义？？？？？？？？？？？？？？？？？？？？？？？？
hist_roi = cv2.calcHist([hsv_roi], channels=[0, 1], mask=None, histSize=[180, 256], ranges=[0, 179, 0, 255])

# 2）直方图归一化，在调用calcBackProject之前，需要对hist_roi进行归一化
cv2.normalize(src=hist_roi, dst=hist_roi, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# 3)反向投影：calcBackProject
backProject = cv2.calcBackProject(images=[hsv_target], channels=[0, 1], hist=hist_roi, ranges=[0, 179, 0, 255], scale=1)

# 4)圆盘卷积
kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5, 5))
backProject = cv2.filter2D(backProject, -1, kernel)

# 5)图像二值化
ret, thresh = cv2.threshold(backProject, thresh=50, maxval=250, type=cv2.THRESH_BINARY)

# 6）抠出目标图像中的感兴趣部分
thresh = cv2.merge((thresh, thresh, thresh))  # 通道合并
res = cv2.bitwise_and(target, thresh)

# plt.imshow(hist_roi)
# plt.show()
# exit(0)

# 展示图片
# cv2.imshow("roi", roi)
# cv2.imshow("hsv_roi", hsv_roi)
# cv2.imshow("target", target)
# cv2.imshow("hsv_target", hsv_target)
# cv2.imshow("backProject", backProject)
cv2.imshow("thresh", thresh)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
