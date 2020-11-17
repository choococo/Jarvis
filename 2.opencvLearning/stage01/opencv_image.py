import cv2


'opencv与numpy一般是一起使用的，opencv中输入的图像使，会自动转成numpy的形式'
'然后输出的也是numpy形式'
img = cv2.imread("../images/1.jpg", 1)                          # 1: color 0:gray -1：alpha
print(img.shape)
print(type(img))

# img = cv2.resize(img, (200, 200))                             # 重新设定个图像的尺寸
img = cv2.resize(img, (img.shape[0]//2, img.shape[1]//2))       # 同上

cv2.line(img, (100, 100), (300, 300), (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
cv2.circle(img, (100, 100), 100, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow("", img)                                             # 显示图像
if cv2.waitKey(0) & 0xFF == ord("q"):                           # 设置取消键,waitKey(0)中0为等待，完全阻塞
    exit(0)
cv2.destroyAllWindows()                                         # 销毁所有的窗口，提高程序的健壮性
# cv2.imwrite("save.jpg", img)                                    # 保存图像


