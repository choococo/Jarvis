import torch
import math


# 计算余弦相似度
a = torch.Tensor([1, 2])
print(a)
b = torch.Tensor([4, 5])
# b = torch.Tensor([1, 2])
print(b)
cos_theta = torch.dot(a, b)/(torch.sqrt(torch.sum(torch.pow(a, 2))) * torch.sqrt(torch.sum(torch.pow(b, 2))))
# cos_theta = torch.dot(a, b)/(torch.sqrt(torch.sum(torch.pow(a, 2))) * torch.sqrt(torch.sum(torch.pow(b, 2))))
print(cos_theta)                                # 这个是相似度

# 把相似度转换成弧度
print(torch.acos(cos_theta))
# 把弧度转换成角度
print(math.degrees(torch.acos(cos_theta)))

print(torch.cosine_similarity(a, b, 0))         # torch中有余弦相似度的计算方法

