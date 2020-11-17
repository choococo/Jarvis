import cv2

'形状匹配：matchShpes()'
img1 = cv2.imread("../images/21.jpg")
img2 = cv2.imread("../images/22.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret1, binary1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours1, hierarchy = cv2.findContours(binary1, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret2, binary2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours2, hierarchy = cv2.findContours(binary2, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

ret = cv2.matchShapes(contours1[0], contours2[0], cv2.CONTOURS_MATCH_I1, 0.0)
print(ret)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
