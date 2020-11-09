import cv2
import matplotlib.pyplot as plt

'图像形态学操作——一定要先二值化，然后再操作'
img1 = cv2.imread("../images/10.jpg", 0)
img2 = cv2.imread("../images/11.jpg", 0)

'''
    1.构造一个特定形状和大小的结构元素(核)，用于形态学操作。
    kernel = getStructuringElement(shape, ksize, anchor=None)
    参数：
    shape: 核的形状。
        MORPH_RECT = 0: 矩形
        MORPH_CROSS = 1: 交叉形
        MORPH_ELLIPSE = 2: 椭圆形
    ksize: 核的结构大小

    2.膨胀: 原图部分区域(A)与核(B)进行卷积，求局部最大值，并将局部最大值赋值给指定像素，从而增长高亮区域。
    dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
        src：表示输入矩阵
        element：表示结构元，即 函数getStructuringElement( )的返回值
        anchor：结构元的锚点，即参考点
        iterations：膨胀操作的次数，默认为一次
        borderType：边界扩充类型
        borderValue：边界扩充值

    3.腐蚀: 与膨胀相反，用局部极小值替换当前像素，从而缩短高亮区域。
    erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)

    4.更多形态学操作
    morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
    参数：
    op: 形态学操作类型。
        cv2.MORPH_DILATE: 膨胀。-->增长高亮部分。
        cv2.MORPH_ERODE: 腐蚀。-->缩短高亮部分。
        cv2.MORPH_GRADIENT: 梯度，(膨胀-腐蚀)。-->提取轮廓。
        cv2.MORPH_OPEN: 开，先腐蚀在膨胀。-->去除噪点。
        cv2.MORPH_CLOSE: 闭，先膨胀再腐蚀。-->填补漏洞。
        cv2.MORPH_TOPHAT: 顶帽/礼帽，(原图-开)。-->获取噪点。
        cv2.MORPH_BLACKHAT: 黑帽，(闭-原图)。-->获取漏洞。
'''

# 1. 获取指定形状和大小的结构元素（核）: getStructuringElement(shape,ksize)
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3, 3))  # 矩形
# kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(3, 3)) # 交叉形/十字形
'''
[[0 1 0]
 [1 1 1]
 [0 1 0]]
'''
# kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5, 5))   # 椭圆形
print(kernel)

# 2. 形态学操作：必须是二值化图，膨胀和腐蚀的部分是白颜色
dilate = cv2.dilate(img1, kernel)  # 膨胀
erode = cv2.erode(img1, kernel)  # 腐蚀

# 使用形态学API，然后调用
morph_dilate = cv2.morphologyEx(img1, cv2.MORPH_DILATE, kernel=kernel)  # 膨胀
morph_erode = cv2.morphologyEx(img1, cv2.MORPH_ERODE, kernel=kernel)  # 腐蚀
morph_gradient = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel=kernel)  # 梯度：膨胀-腐蚀，用于提取轮廓

# 开操作_用于取出白色噪点
morph_open = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel=kernel)  # 开操作：先腐蚀再膨胀 ，用于去噪
morph_erode2 = cv2.morphologyEx(img2, cv2.MORPH_ERODE, kernel=kernel)  # 先腐蚀，去掉白色噪点
morph_dilate2 = cv2.morphologyEx(morph_erode2, cv2.MORPH_DILATE, kernel=kernel)  # 膨胀

# 闭操作_用于补充漏洞（补充白色）
morph_close = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel=kernel)  # 闭操作：先膨胀取出漏洞，再腐蚀还原，用于填补漏洞
morph_dilate3 = cv2.morphologyEx(img2, cv2.MORPH_DILATE, kernel=kernel)  # 先膨胀补充漏洞
morph_erode3 = cv2.morphologyEx(morph_dilate3, cv2.MORPH_ERODE, kernel=kernel)  # 用于还原

# 顶帽/礼帽操作_用于获取噪点(原图（有噪点）-开运算（没有噪点）)
morph_tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel=kernel)

# 黑帽操作_用于获取漏洞（闭运算（补漏洞）-原图（有漏洞））
morph_blackhat = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel=kernel)

# cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
# cv2.imshow("dilate", dilate)
# cv2.imshow("erode", erode)
# cv2.imshow("morph_dilate", morph_dilate)
# cv2.imshow("morph_erode", morph_erode)
# cv2.imshow("morph_gradient", morph_gradient)
# cv2.imshow("morph_open", morph_open)
# cv2.imshow("morph_erode2", morph_erode2)
# cv2.imshow("morph_dilate2", morph_dilate2)
# cv2.imshow("morph_close", morph_close)
# cv2.imshow("morph_dilate3", morph_dilate3)
# cv2.imshow("morph_erode3", morph_erode3)
cv2.imshow("morph_tophat", morph_tophat)
cv2.imshow("morph_blackhat", morph_blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
