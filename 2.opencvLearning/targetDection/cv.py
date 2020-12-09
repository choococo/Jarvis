import cv2

# file = r"../images/000004.jpg"
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
# 110 122 234 324
# 18 61 85 127 177 265 319 326 353 420 469 471 482 547 603 649 664 708 733 786 865
#         127 177 353 420 471 482 603 664 733 786 865
# 18 85       177 353 420 471 482 603 664 733 786 865
# 1217 1276 1814 1992 2283 3256 3493 4234 4416 4653 4683 4753 5055 5274 5302 5806 6000 7242 7712 8887 8956 9214 10050 10237 10271 11987 12147
# 4004 4368 4467 4498 4499 4961 5143 5145 5474 5553 5752 5864 5952 5971 5987 6751 6911 6937 6992 7668 7799 7949 8079 8530 8713 8899 8950 9017 9209 9728 9912   0.3-0.4
# 1276 1992 3493 4683 5055 6000 8887    0.2-0.3
# 1002 1217 1814 2283 3256 4234 4416 4653 4753 5274 5302 5806 7242 7712 8956 9214    0.1-0.2
# 1415 1583 2016 2099 2332 2349 2856 2998 3009 3152 3392 3427 3788 4098 4531 4959 4973 5214 5387 5421 5967 6078 6087 6227 6262 6610 6727 6799 6997 7111 7327 7430 7533 7612 7630 7772 8329 8361 8422 9134 9758   0-0.1
i = 2016
old_path = r"./label/list_bbox_celeba.txt"
new_path = r"./label/list_new_bbox.txt"
# image  = cv2.imread(f"F:\BaiduNetdiskDownload\img_celeba\img_celeba/00{i}.jpg")
image = cv2.imread("images/000001.jpg")
# j = 0
# with open(old_path, "r") as f:
#     old = f.readlines()[2:]
# with open(new_path, "r") as f2:
#     new = f2.readlines()
# i = i-1
# x1, y1, w1, h1 = map(int, old[i].split()[1:])
# x2, y2, w2, h2 = map(int, new[i].split()[1:])
# cv2.minAreaRect((137,160,137+199,160+184))
# 百度AI开放平台上的测试
cv2.rectangle(image, (137, 160 - 10), (137 + 199, 160 + 184), (0, 255, 0), 2)
# cv2.rotatedRectangleIntersection(image,(137,160),(137+199,160+184))
# cv2.rectangle(image,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
# cv2.rectangle(image,(x2,y2),(x2+w2,int((y2+h2)*1.1)),(255,0,0),2)

# cv2.namedWindow("",cv2.WINDOW_NORMAL)
cv2.imshow("", image)
cv2.waitKey(0)

# 000005.jpg 234 106 136 136
# 140  84 195 270
# cv2.rectangle(image, (41, 204), (41 + 57, 204 + 57), (0, 255, 0), 2)
# cv2.rectangle(image, (140, 84), (140 + 195, 84 + 270), (255, 0, 0), 2)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
