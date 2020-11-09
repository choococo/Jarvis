# Numpy中的FFT（Fast Fourier Transform）
import cv2
import numpy as np
import matplotlib.pyplot as plt

'快速傅里叶变换'
'FFT:时域是对每个像素值的统计，频域是对像素之间的差异值的统计'
img = cv2.imread("../images/1.jpg")
# 0. 抓换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape
print(rows, cols)

# 1. 快速傅里叶变换：空域->频域
fft = np.fft.fft2(gray)  # 傅里叶变换，参数为灰度图
print(fft.shape)

# 2. 中心化：将低频信号移动到图像中心
fftshift = np.fft.fftshift(fft)
print(fftshift.shape)
print(np.min(np.abs(fftshift)))  # 绝对值最低频的信号
print(np.max(fftshift), np.min(fftshift))  # 最高频信号，最低频信号

# 获取振幅谱（展示图片用）:np.log()是为了把值 压缩在[0, 255]附近
magnitude_spectrum = np.log(np.abs(fftshift))
print(np.max(magnitude_spectrum), np.min(magnitude_spectrum))

# 3.滤波操作值高通滤波（去低频，保高频）
fftshift[rows // 2 - 50:rows // 2 + 50, cols // 2 - 50:cols // 2 + 50] = 0
print(fftshift.shape)

# 4. 去中心化：将剩余的低频和高频的位置还原
ifftshift = np.fft.ifftshift(fftshift)
print(ifftshift)    # 复数

# 5. 逆傅里叶变换：频域->空域
ifft = np.fft.ifft2(ifftshift)

# 6.二维向量取模（幅值）
img_back = np.abs(ifft)

# 结合matplotlib展示多张图片
plt.figure(figsize=(10, 10))
plt.subplot(221), plt.imshow(gray, cmap="gray"), plt.title("Input Gray Image")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap="gray"), plt.title("Magnitude Spectrum")
plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(img_back, cmap="gray"), plt.title("Image after HPF")
# plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(img_back), plt.title("Result in JET")  # 默认cmap='jet'
# plt.xticks([]), plt.yticks([])
plt.show()

# cv2.imshow("gray", gray)
# cv2.imshow("magnitude_spectrum", magnitude_spectrum)    # 使用opencv显示有问题
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"DFT"
