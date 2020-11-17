import cv2

file = r"../images/000004.jpg"
# path = r"./haarcascades/haarcascade_frontalface_default.xml"
# face_cascade = cv2.CascadeClassifier(path)
# cap = cv2.VideoCapture(file)
#
# while True:
#     ret, img = cap.read()
#     if ret:
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         # 脸部检测
#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             # roi_gray = gray[y:y + h, x:x + w]
#             # roi_color = img[y:y + h, x:x + w]
#
#         # 显示原图像
#         cv2.imshow('img', img)
#     # 按q键退出while循环
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
# 95  71 226 313
# 622 257 564 781
#110 122 234 324
image  = cv2.imread("./images/000014.jpg")
cv2.rectangle(image, (110, 122), (110 + 234, 122 + 324), (255, 0, 0), 2)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
