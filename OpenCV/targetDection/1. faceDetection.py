import cv2

"""
利用opencv中的已经封装好的xml，实现人脸的侦测, 只能搞一些正脸，侧脸是检测不到的
"""
# xml_path = r"./haarcascades/haarcascade_frontalface_alt2.xml"
# xml_path = r"./haarcascades/haarcascade_frontalface_default.xml"
face_xml_path = r"./haarcascades/haarcascade_frontalface_alt.xml"
eye_xml_path = r"./haarcascades/haarcascade_eye.xml"
face_cascade = cv2.CascadeClassifier(face_xml_path)
eye_cascade = cv2.CascadeClassifier(eye_xml_path)
# image = cv2.imread("../images/1.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(3, 3))
#
# print("发现{0}个人脸".format(len(faces)))
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# path = r"../images/1.mp4"
# path = r"../images/01.jpg"
path = r"./images/000005.jpg"
cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(3, 3))

        print("发现{0}个人脸".format(len(faces)))
        # 脸部检测
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h + 10), (255, 0, 0), 2)
            roi_face = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # eyes = eye_cascade.detectMultiScale(roi_face)
            # print("eye={0}".format(len(eyes)))
            # for (e_x, e_y, e_w, e_h) in eyes:
            #     cv2.rectangle(roi_color, (e_x, e_y), (e_x + w, e_y + h), (0, 255, 0), 2)
            # 显示原始图像
            cv2.imshow("image", frame)
        # 按q键退出while循环
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
