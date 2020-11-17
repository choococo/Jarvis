import cv2
import numpy as np

'霍夫变换'
"""
1. 轮廓检测算法公式检测出轮廓，使用参数作为坐标系
    1) 直线检测
    lines = cv2.HoughLines(image, rho, theta, threshold)
    
    参数：
    image: 单通道中的二进制图像
    rho: (ρ，θ)中ρ的精度。
    theta: (ρ，θ)中θ的精度。
    threshold: 阈值，(ρ，θ)对应的最低投票数。>=threshold被检测为一条线。
    2）圆检测
    circles = cv2.HoughCircles(images, method, dp, minDist, circles=None, param1=None, maxRadius=None)
    
    参数：
    method:定义检测图像中圆的方法，目前唯一的实现的方法是HOUGH_GRADIENT
    dp: 累加器分辨率与图像分辨率的反比
        dp=1,则累加器与输入图像具有相同的分辨率; dp=2,累加器有一般的宽度和高度
    minDist:该参数是让算法能明显区分的两个不同圆之间的最小距离
    param1:该参数是让算法能明显区分的两个不同圆之间的最小的距离
    param2:HOUGH_GRADIENT方法的累加器的阈值(最低投票数),阈值越小，检测到的圈子越多
    minRadius:最小圆半径
    maxRadius:最大圆半径
"""

'1. 直线检测'
image = cv2.imread("../images/24.jpg")

# 1）进行高斯模糊
image = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=50)

# 2）轮廓检测算法检测出轮廓
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 150)

# 3) 投影到Hough空间进行形状检测
# 任何一条直线都可以使用(ρ，θ)术语进行表示
# -1）先定义衣蛾累加器，(ρ，θ)对应直线，ρ和θ都分别依次增大(根据精度),计算每对(ρ，θ)的投票数
#    其中，ρ以像素作为单位，θ以弧度作为单位，rho和theta是ρ和θ的精度
# -2) 然后，根据threshold(阈值， 最低投票数)来判断是否归为一条直线
lines = cv2.HoughLines(image=edges, rho=1, theta=np.pi / 100, threshold=100)  # 隔一个长度单位的采样，角度

# 画线
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 - 1000 * (b))  # 直线的起点横坐标
    y1 = int(y0 - 1000 * (a))  # 直线的起点纵坐标
    x2 = int(x0 + 1000 * (b))  # 直线的终点横坐标
    y2 = int(y0 + 1000 * (a))  # 直线的终点横坐标
    # # 画线
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)

'2. 圆检测'
img = cv2.imread("../images/25.jpg")

# (1) 轮廓检测算法检测出轮廓
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(img, 50, 100)
# cv2.imshow("edges", edges)
# circles = cv2.HoughCircles(image=edges, method=cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=10, param2=20, minRadius=20, maxRadius=500)
# circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100, param1=10, param2=20, minRadius=20, maxRadius=500)
# print(circles)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100,#隔1度的采样，第一个圆和第二个的距离
                           param1=10, param2=20, minRadius=20, maxRadius=500)#双边阈值（断裂），最小最大半径
# 画圆
if not circles is None:
    circle = np.around(circles)
    print(circle)
    for i in circle[0, :]:
        cv2.circle(img, center=(i[0], i[1]), radius=int(i[2]), color=(0, 255, 0), thickness=2)
# if not circles is None:
#     circle = np.around(circles)
#     for i in circle[0, :]:
#         cv2.circle(img, (i[0], i[1]), int(i[2]), (0, 255, 0), 2)
# cv2.imshow("edges", edges)
# cv2.imshow("img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
