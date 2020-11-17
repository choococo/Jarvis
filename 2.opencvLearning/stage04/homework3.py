import cv2

image = cv2.imread("")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

gaussian = cv2.GaussianBlur(thresh, ksize=(5, 5), sigmaX=0)

contours, hierarchy = cv2.findContours(gaussian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(contours[0]))

for i in range(len(contours[0])):
    x, y, w, h = cv2.boundingRect(contours[i])
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()