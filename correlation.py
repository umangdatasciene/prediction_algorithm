import numpy as np

x = np.array([-2, -1, 0, 1, 2])
y = np.array([4, 1, 3, 2, 0])
correlation = np.corrcoef(x, y)

print("Corelation between x and y is : ",correlation)