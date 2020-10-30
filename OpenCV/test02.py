import cv2
from PIL import Image, ImageFont


cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1.m3u8")
width, height = cap.get(3), cap.get(4)
print(width, height)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.rectangle(frame, (100, 100), (300, 300), color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(frame, text="你好".encode("utf-8"),org=(300, 300), fontScale=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(0, 255, 0), thickness=2)
        # cv2.putText(frame, text="hello",org=(300, 300), fontScale=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(0, 255, 0), thickness=2)
        cv2.imshow("", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cv2.destroyAllWindows()

