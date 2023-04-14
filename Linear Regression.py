import numpy as np
import pandas as pd

x=np.array ([1,2,4,5,6,7,8,10])
y=np.array ([2,4,6,7,9,11,12,14])

x_mean=np.mean(x)
y_mean=np.mean(y)

n=0
d=0
for i in range (len(x)):
    n+=(x[i]-x_mean)*(y[i]-y_mean)
    d+=(x[i]-x_mean)**2
slope=n/d
intercept=y_mean-(slope*x_mean)
print ("Linear Regression")
print (slope)
print (intercept)