import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1.m3u8")
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.Canny(frame, 200, 200)
    cv2.imshow('1', frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()


