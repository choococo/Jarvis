import cv2
import numpy as np

'模板匹配'
'''
函数：cv2.matchTemplate(), cv2.minMaxLoc()
1) 模板匹配，得到匹配灰度图
    res = cv2.matchTemplate(image, templ, method, resutl=None, mask=None)
    
    参数：
    image：输入图像
    templ：模板图像
    method：模板匹配的方法，包括：
    - CV_TM_SQDIFF 平方差匹配法：该方法采用平方差来进行匹配；最好的匹配值为0，匹配最差，匹配值越大
    - CV_TM_SQDIFF_NORMED 相关匹配法：该方法采用乘法操作；数值越大表明匹配程度越好。
    - CV_TM_CCORR 相关系数匹配法；1表示完美的匹配；-1表示最差的匹配。
    - CV_TM_CCORR_NORMED 归一化平方差匹配法
    - CV_TM_CCOEFF 归一化相关匹配法
    - CV_TM_CCOEFF_NORMED 归一化相关系数匹配法
2）获取最小和最大像素值及它们的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxlos(res)
3) 最后，将匹配的区域标记出来
    cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
'''

# 1. 单对象匹配：原图中仅有一个与模板匹配
img = cv2.imread("../images/16.jpg")  # 梅西踢足球的照片
template = cv2.imread("../images/17.jpg")  # 梅西的头像
h, w, c = template.shape
print(h, w, c)

# 1). 匹配模板，得到匹配灰度图(这里会自动将图片转为灰度图)
# res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_CCOEFF)  # 归一化相关匹配法
# res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_CCORR_NORMED)  # 归一化[-1, 1], 1表示100%匹配
# res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_CCORR)  # 效果不好
res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_CCORR_NORMED)  # 归一化区域[0,1]一般使用这个就行
# res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_SQDIFF)  # 效果不好，最小值是最匹配 区域
# res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_SQDIFF_NORMED)  # 效果不好

cv2.imshow("res", res)  # 这里是模板灰度图, 比较抽象
print(res.shape)

# 2).获取最小和最大像素及它们的位置(坐标)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)  # -9535398.0 18226688.0 (102, 212) (223, 85)

# 3) 最后将匹配的模板区域标记出来
# 匹配类型是TM_CCOEFF、TM_CCOEFF_NORMED、TM_CCORR、TM_CCORR_NORMED时，最大值是最匹配区域
# 匹配类型是TM_SQDIFF、TM_SQDIFF_NORMED时，最小值是最匹配区域
cv2.rectangle(img, (max_loc[0], max_loc[1]), (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), thickness=2)
# 匹配类型是TM_SQDIFF、TM_SQDIFF_NORMED时，最小值是最匹配区域
# cv2.rectangle(img, (min_loc[0], min_loc[1]), (min_loc[0] + w, min_loc[1] + h), color=(0, 0, 255), thickness=2)
cv2.imshow("img", img)

# 2. 多对象匹配：原图中有多个与模板匹配
img = cv2.imread("../images/19.jpg")
template = cv2.imread("../images/20.jpg")
h, w, c = template.shape
print(h, w, c)

# 1) 匹配模板，得到匹配的灰度图
res = cv2.matchTemplate(image=img, templ=template, method=cv2.TM_CCORR_NORMED)
print(res.shape)
# cv2.imshow("res", res)

# 2) 当匹配元素>=0.95时，认为是匹配的
locs = np.where(res >= 0.95)
print(locs)
# 加入*是为了扩展解包，相当于解压的功能与zip相反去掉(array([...]), array([...])), 直接变成[...] [...]
print(*locs[::-1])  # ::-1是为了把hw->wh,图片是hwc,要转换成whc,这样得到的就是(x, y)而不是(y, x)
# 这里对已经转换为[...] [...] 的值进行zip()压缩组，通过循环遍历得到[x1, y1]...[xn, yn]
for pt in zip(*locs[::-1]):
    x, y = pt[0], pt[1]
    # 3）最后，利用循环将所有的区域标记出来
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
# cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
