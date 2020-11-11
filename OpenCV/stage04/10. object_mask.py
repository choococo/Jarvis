import cv2
import numpy as np

'对象掩码mask'
img = cv2.imread("../images/23.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(image=binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros_like(img, np.uint8)
cv2.drawContours(image=mask, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=-1)

pixel_points = np.transpose(np.nonzero(mask))
print(pixel_points)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
