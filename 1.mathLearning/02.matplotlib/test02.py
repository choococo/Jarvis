import matplotlib.pyplot as plt
import numpy as np

# '画柱状图、条形图、饼图'
# x = [5,8,10]
# y = [9,7,3]
# x1 = [6,9,4]
# y1 = [8,6,4]
# plt.bar(x,y)
# plt.bar(x1,y1)
# plt.show()

# '条形分布图'
# x = np.random.randn(2000)
# plt.hist(x,200)
# plt.show()

# '2D点图'
# x = np.random.randn(1000)
# y = np.random.randn(1000)
# plt.hist2d(x,y,100)
# plt.show()

# '饼图'
plt.rcParams["font.sans-serif"] = ["SimHei"]
labels = ["教育", "医疗", "餐饮", "交通", "房贷", "车贷", "其他"]
sizes = [10, 7, 5, 5, 60, 8, 5]
explode = (0, 0, 0, 0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, autopct="%.2f%%", shadow=True, startangle=180)
plt.title("8月份家庭月支出饼图")
plt.show()


