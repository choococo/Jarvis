import datetime
import cv2
import os

ip = '192.168.3.160'.replace(".", "_")
# rtsp = 'rtsp://admin:admin@192.168.3.160:554/1/1'
rtsp = "http://ivi.bupt.edu.cn/hls/cctv1.m3u8"
# 初始化摄像头
cap = cv2.VideoCapture(rtsp)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

frame_count = 0
while cap.isOpened():
    isSuccess, frame = cap.read()
    if isSuccess:
        if frame_count % 120 == 0 or frame_count == 0:
            frame_count = 0
            i = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = str(i) + '-' + ip + '.avi'
            print(filename)
            video_writer = cv2.VideoWriter(filename, fourcc, 24, size)

        video_writer.write(frame)
        frame_count = frame_count + 1
        print(frame_count)
        if frame_count % 120 == 0:
            video_writer.release()
            portion = os.path.splitext(filename)
            newname = portion[0] + '.mp4'
            os.rename(filename, newname)
        # cv2.imshow('show', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
