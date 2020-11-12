import cv2

'图像掩码操作'
img1 = cv2.imread("../images/1.jpg")
img2 = cv2.imread("../images/7.jpg")
print(img1)
img2gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
print(img2gray)
ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

mask_inv = cv2.bitwise_not(mask)                                                    # 取反

# 利用掩码进行与操作，即掩码图像白色区域是对需要处理的图像像素的保留，黑色区域是对需要处理图像像素的剔除
img1_bg = cv2.bitwise_and(img1, img1, mask=mask_inv)

# cv2.imshow("0", img2)
cv2.imshow("0", img2gray)
cv2.imshow("", mask)
cv2.imshow("1", mask_inv)
cv2.imshow("2", img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()