import cv2
import numpy as np

'图像混合方式一：'
image1 = cv2.imread("../images/1.jpg")

image2 = np.uint8(np.random.randn(image1.shape[0], image1.shape[1], image1.shape[2]))


image3 = np.uint8(np.zeros([image1.shape[0], image1.shape[1], image1.shape[2]]))

cv2.putText(image3, 'beautiful girl', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5, lineType=cv2.LINE_AA)

dst = cv2.addWeighted(src1=image1, alpha=0.5, src2=image3, beta=1, gamma=15)
cv2.imshow("", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
