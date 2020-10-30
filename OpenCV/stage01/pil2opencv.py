import cv2
from PIL import Image
import numpy as np

'从PIL转到opencv——RGB2BGR'
img = Image.open("../images/1.jpg")
img_arr = np.array(img)
img_arr = cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)                  # C通道颜色的转换
# cv2.imshow("", img_arr)
#
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     exit(0)
# cv2.destroyAllWindows()



'从opencv到PIL——BGR2RGB'
img = cv2.imread("../images/1.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(type(img))
img = img[..., ::-1]                                                # 通道颜色转换的第二种方法
img = Image.fromarray(img)
img.show()



