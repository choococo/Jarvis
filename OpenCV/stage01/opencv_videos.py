import cv2


path = r"../images/1.mp4"
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)
    else:
        break
cap.release()
cv2.destroyAllWindows()