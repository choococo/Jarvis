import cv2
import matplotlib.pyplot as plt

'图像形态学操作'
img1 = cv2.imread("../images/10.jpg", 0)
img2 = cv2.imread("../images/11.jpg", 0)

'''
    1. 构造一个特定形状大小的结构元素(核)，用于形态学操作
    kernel = getStructuringElement(shape, ksize, anchor=None)
    参数：
    shape:核的形状
        MORPH_RECT = 0: 矩形
        MORPH_CROSS = 1: 交叉形
        MORPH_ELLIPSE = 2: 椭圆形
    ksize:核的大小
    
    2.膨胀: 原图部分区域(A)与核(B)进行卷积，求局部最大值，并将局部最大值赋值给指定像素，从而增长高亮区域。
    dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
    
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
