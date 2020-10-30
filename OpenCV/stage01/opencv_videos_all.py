import cv2


input_path = r"../images/1.mp4"
output_path = r"../images/output.mp4"
cap = cv2.VideoCapture(input_path)                      # 创建视频对象

# fourcc = cv2.VideoWriter_fourcc(*"XVID")              # 这个格式和下面格式有的在Linux系统中只要一种是好使的
fourcc = cv2.VideoWriter_fourcc(*"DIVX")                # 写入视频常用的格式,为MP4格式
fps = cap.get(cv2.CAP_PROP_FPS)                         # 获取当前视频的帧数
print(fps)

w, h = int(cap.get(3)), int(cap.get(4))                 # 读取视频的宽和高
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h)) # 创建视频写入格式，大小和帧数的对象


while cap.isOpened():
    ret, frame = cap.read()                             # 捕获每一帧图像，ret为每一帧读取的布尔值, frame是每一帧画面
    if ret:                                             # ret == True为有图片可读
        frame = cv2.resize(frame, (w, h))               # 可以对视频大小重新设计尺寸，上面的写入兑现的尺寸也一定要修改
        # 画框框
        cv2.rectangle(frame, (200, 50), (300, 150), (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
        # 写文字
        cv2.putText(frame, "beautiful girl", (100, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(0, 0, 255), fontScale=1, thickness=1, lineType=cv2.LINE_AA)

        # out.write(frame)
        cv2.imshow("", frame)

        if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
