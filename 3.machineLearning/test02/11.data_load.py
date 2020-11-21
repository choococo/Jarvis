import numpy as np

try:
    file = open("data/test.txt")
    str = np.loadtxt("data/test.txt")
    print(str)
    print(file)
except RuntimeError as e:
    print(e)
finally:
    file.close()

