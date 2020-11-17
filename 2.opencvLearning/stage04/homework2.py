import cv2


path = r"D:\test01.mp4"
cap = cv2.VideoCapture(path)
# cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1.m3u8")
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # gray = cv2.Canny(gray, 100, 200)
        # gray = cv2.convertScaleAbs(gray, alpha=2, beta=10)
        kerner = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kerner)
        # gray = cv2.GaussianBlur(close, (15, 215), 0)

        ret, binary_inv = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # print(binary_inv)
        # ret, binary_inv = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        x, y, w, h = cv2.boundingRect(binary_inv)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        cv2.imshow('frame0', gray)
        cv2.imshow('frame1', frame)
        cv2.waitKey(40)
    else:
        break
cap.release()
cv2.destroyAllWindows()