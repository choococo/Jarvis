import cv2
import numpy as np

# bg = cv2.imencode(np.fromfile(""))

bg = cv2.imread("../images/bg1.png")
logo = cv2.imread("../images/logo1.png")
# logo2 = cv2.imread("../images/logo2.jpg")
rows, cols, c = logo.shape
logo = cv2.resize(logo, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_NEAREST)


# 1. 将logo灰度化
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# 2. 进行阈值操作
ret, thresh = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh1", thresh)
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)
mask_inv = cv2.bitwise_not(thresh)
cv2.imshow("thresh", thresh)

# 4. 提取roi区域，背景图的左上角
roi = bg[:logo.shape[0], :logo.shape[1]]
# cv2.imshow("roi", roi)
# # and操作
roi_and_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow("roi_and_bg", roi_and_bg)
roi_and_bg2 = cv2.bitwise_and(logo, logo, mask=thresh)
cv2.imshow("roi_and_bg2", roi_and_bg2)

dst = cv2.add(roi_and_bg, roi_and_bg2)
cv2.imshow("dst", dst)
bg[:logo.shape[0], :logo.shape[1]] = dst

# cv2.imshow("clean_thresh",
#
#
#
# clean_thresh)
# cv2.imshow("logo2", logo2)
# cv2.imshow("logo", roi_and_bg2)
cv2.waitKey(0)
cv2.destroyAllWindows()
