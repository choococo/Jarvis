import cv2
import os

SRC_DIR = "data2"
DST_DIR = "data3"

face_cascade = cv2.CascadeClassifier('opencv/haarcascades/haarcascade_frontalface_default.xml')

for person_dir in os.listdir(SRC_DIR):
    label = int(person_dir)
    label_dir = os.path.join(DST_DIR, str(label))
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)
    for pic_filename in os.listdir(os.path.join(SRC_DIR, person_dir)):
        img = cv2.imread(os.path.join(SRC_DIR, person_dir, pic_filename))
        print(img.shape)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        boxes = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(boxes) == 1:
            x, y, w, h = boxes[0]
            corp = img[y:y + h, x:x + w]
            cv2.imwrite(os.path.join(label_dir, pic_filename), corp)
