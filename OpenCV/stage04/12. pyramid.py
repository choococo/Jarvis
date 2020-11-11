import cv2

'图像金字塔'
# 1. 高斯金字塔
img = cv2.imread("../images/1.jpg")
for i in range(5):
    cv2.imshow(f"img{i}", img)
    img = cv2.pyrDown(img)
    img = cv2.pyrUp(img)

# 2. 拉普拉斯金字塔
img = cv2.imread("../images/1.jpg")
img_down = cv2.pyrDown(img) # 缩小
img_up = cv2.pyrUp(img_down) # 缩小后放大，变模糊，丢失轮廓信息

img_new = cv2.subtract(img, img_up) # 做减法获取轮廓的信息
cv2.imshow("img_new", img_new)

# 展示图片
for i in range(3):
    cv2.imshow(f"img{i}", img_new)
    img_new = cv2.pyrDown(img_new)
    img_new = cv2.pyrUp(img_new)

cv2.waitKey(0)
cv2.destroyAllWindows()