import cv2

# 1. 读取图片
rawImage = cv2.imread("../images/27.jpg")

# 2. 高斯模糊
image = cv2.GaussianBlur(rawImage, (3, 3), 0)

# 3. 图片灰度化
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# 4. Sobel 算子(X方向)
Sobel_x = cv2.Sobel(image, cv2.CV_16S, dx=1, dy=0)
Sobel_y = cv2.Sobel(image, cv2.CV_16S, dx=0, dy=1)

abs_x = cv2.convertScaleAbs(Sobel_x)
abs_y = cv2.convertScaleAbs(Sobel_y)

image = cv2.addWeighted(src1=abs_x, alpha=0.5, src2=abs_y, beta=0.5, gamma=0)
# cv2.imshow("image", image)

# 5. 二值化处理
ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
# cv2.imshow("thresh", thresh)

# 6. 闭操作:先膨胀再腐蚀，将目标可以练成一个整体，然后进行后续的轮廓的提取
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(3, 3))
image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernelX)
# cv2.imshow("closed", image)

# 7. 膨胀腐蚀
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(20, 1))
kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(1, 20))

image = cv2.dilate(image, kernelX) # x轴上膨胀，在x轴上连续
# cv2.imshow("2", image)
image = cv2.erode(image, kernelX) # 在x轴上进行腐蚀，还原，但是其实没有什么效果，对于需要提取的目标区域
# cv2.imshow("3", image)
image = cv2.erode(image, kernelY) # 在y轴上进行腐蚀，切断x上的数据，在目标的地方，主要是为了去除不连续的，留下连续的
# cv2.imshow("4", image)
image = cv2.dilate(image, kernelY) # 在y轴上膨胀，使得需要提取的目标区域，尽量还原原来的形状
# cv2.imshow("5", image)

# 8. 查看轮廓
contours, hierarchy = cv2.findContours(image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
for item in contours:
    rect = cv2.boundingRect(item)
    x = rect[0]
    y = rect[1]
    w = rect[2]
    h = rect[3]
    if w > (h * 2):
        # 裁剪区域图片
        chepai = rawImage[y:y + h, x:x + w]
        cv2.imshow('chepai' + str(x), chepai)

# 9. 在原图上绘制轮廓
cv2.drawContours(rawImage, contours, -1, (0, 0, 255), thickness=3)
cv2.imshow("image1", rawImage)
cv2.waitKey(0)
cv2.destroyAllWindows()