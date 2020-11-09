# Numpy中的FFT（Fast Fourier Transform）
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
图像的时域(分析每个时间点、空间位置的一个点)和频域(分析两个点、线之间的变化：梯度)
梯度大的是图像的轮廓，梯度小的是背景内容
滤波是将信号中特定的波段频率滤除的操作，是抑制和防止干扰的一项重要措施
"""
'快速傅里叶变换'
'FFT:时域是对每个像素值的统计，频域是对像素之间的差异值的统计'
"""
傅里叶变换，经常被用来分析不同滤波器的频率特性，我们可以使用2D离散傅里叶变换DFT分析图像的频域特性。
实现一个DFT的一个快速算法被称为快速傅里叶变换(FFT)。
高频分量：边界和噪声是高频分量，变化的幅度非常的大，低频分量变换的幅度比较缓慢，也就是大片色块的地方
"""
'numpy 中的傅里叶变换'
img = cv2.imread("../images/16.jpg")
# 0. 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape
print(rows, cols)
# 1. 快速傅里叶变换：空域->频域
# np.fft.fft2()可以对信号频率转换，输出结果是一个复杂的数组,里面由复数构成
# 函数的第一个参数是输入图像，要求是灰度格式。第二个参数是可选择的，决定输出数组的大小，
# 输入输出的图像大小一样，如果输出结果比输入图像大，输入图像就需要在进行FFT前补0.
# 如果输出的结果比输入图像小的话，输入图像就会被切割
fft = np.fft.fft2(gray)  # 傅里叶变换，参数为灰度图
# print(fft.shape)
# print(fft[fft > 0])

# 2. 中心化：将低频信号移动到图像中心
# 上面得到了频率为0的部分（直流分量）在输出图像的左上角，如果想让它（直流分量）在输出图像的中心，
# 还需要将结果沿着两个方向平移N/2.(这样更容易分析)
fftshift = np.fft.fftshift(fft)
# print(fftshift.shape)
# print(np.min(np.abs(fftshift)))  # 绝对值最低频的信号
# print(np.max(fftshift), np.min(fftshift))  # 最高频信号，最低频信号

# 获取振幅谱（展示图片用）:np.log()是为了把值 压缩在[0, 255]附近
# 在频率变换之后，就可以构建振幅谱了，按照下面的公式进行振幅谱的构建就行了
magnitude_spectrum = 20 * np.log(np.abs(fftshift))
print(np.max(magnitude_spectrum), np.min(magnitude_spectrum))

# 3.滤波操作值高通滤波（去低频，保高频）？？？？？？？？？？？？？？？
fftshift[rows // 2 - 50:rows // 2 + 50, cols // 2 - 50:cols // 2 + 50] = 0
# fftshift[rows // 2 - 30:rows // 2 + 30, cols // 2 - 30:cols // 2 + 30] = 0
# print(fftshift.shape)

# 4. 去中心化：将剩余的低频和高频的位置还原
ifftshift = np.fft.ifftshift(fftshift)
# print(ifftshift)  # 复数

# 5. 逆傅里叶变换：频域->空域
ifft = np.fft.ifft2(ifftshift)

# 6.二维向量取模（幅值）
img_back = np.abs(ifft)  # 防止有复数，取模

# 结合matplotlib展示多张图片
plt.figure(figsize=(10, 10))
plt.subplot(221), plt.imshow(gray, cmap="gray"), plt.title("Input Gray Image")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap="gray"), plt.title("Magnitude Spectrum")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img_back, cmap="gray"), plt.title("Image after HPF")
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_back), plt.title("Result in JET")  # 默认cmap='jet'
plt.xticks([]), plt.yticks([])
plt.show()

'''
上面显示高通滤波其实是一种边界检测操作，就是像梯度一样的
'''

# cv2.imshow("gray", gray)
# cv2.imshow("magnitude_spectrum", magnitude_spectrum)    # 使用opencv显示有问题
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"DFTOpenCV中的傅里叶变换——离散傅里叶变换"
# 频率派和贝叶斯学派
# OpenCV中的DFT(Discrete Fourier Transform)   离散傅里叶变换
img = cv2.imread("../images/1.jpg")

# 0. 转化为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape

# 1. DFT离散傅里叶变换，空域->频域
# cv2.DFT_COMPLEX_OUTPUT 以复数的形式输出，这里是两个通道
dft = cv2.dft(src=np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)  # src为灰度图, 并且是numpy.float32的形式
print(dft.shape)

# 2. 中心化：将低频移动到图像中心
fftshift = np.fft.fftshift(dft)

# 获取振幅谱(展示图片使用), numpy.log()为了将值限制在[0, 255]
magnitude_spectrum = np.log(cv2.magnitude(fftshift[:, :, 0], fftshift[..., 1]))

# 3. 滤波操作之高通滤波(去除低频，保留高频，相当于保留有梯度的地方，保留轮廓信息)
# Opencv中的dft与前面不同的就是双通道的
# mask = np.zeros((rows, cols, 2), dtype=np.uint8)
# mask[rows // 2 - 30:rows // 2 + 30, cols // 2 - 30:cols // 2 + 30] = 1
fftshift[rows // 2 - 30:rows // 2 + 30, cols // 2 - 30:cols // 2 + 30] = 0
# fftshift = fftshift * mask

# 4. 去中心化：将低频和高频位置还原
ifftshift = np.fft.ifftshift(fftshift)

# 5. 逆傅里叶变换：频域->空域
idft = cv2.idft(ifftshift)
print(idft.shape)  # (540, 960, 2)

# 6. 二维向量取模（幅值）
img_back = cv2.magnitude(idft[..., 0], idft[..., 1])  # 把两个通道组合在一起
print(img_back.shape)

# 结合matplotlib展示多张图片
# plt.figure(figsize=(10, 10))
# plt.subplot(221), plt.imshow(gray, cmap="gray"), plt.title("Input Gray Image")
# plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(magnitude_spectrum, cmap="gray"), plt.title("Magnitude Spectrum")
# plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(img_back, cmap="gray"), plt.title("Image after LPF")
# plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(img_back), plt.title("Result in JET")  # 默认cmap='jet'
# plt.xticks([]), plt.yticks([])
# plt.show()
