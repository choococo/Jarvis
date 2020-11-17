from sklearn import datasets, neighbors, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

'查看数据集中其他的数据集的数据'
# 1.查看鸢尾花数据集的数据
iris = datasets.load_iris()
x, y = iris.data, iris.target
print(x, y)
print(x.shape, y.shape) # (150, 4) (150,)

# 2. 查看红酒的数据集的数据
wine = datasets.load_wine()
x, y = wine.data, wine.target
print(x, y)
print(x.shape, y.shape) # (178, 13) (178,)

# 3.查看波士顿房价的数据集数据
boston = datasets.load_boston()
x, y = boston.data, boston.target
print(x, y)
print(x.shape, y.shape) # (506, 13) (506,)