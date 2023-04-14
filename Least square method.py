import numpy as np
def least_square(x,y):
    n=len(x)
    sum_x=np.sum(x)
    sum_y=np.sum(y)
    sum_xy=np.sum(x*y)
    sum_x2=np.sum(x**2)
    a=(sum_y*sum_x2-sum_x*sum_xy)/(n*sum_x2-sum_x**2)
    b=(n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
    return a,b
x=np.array([1,2,4,6,7])
y=np.array([1,3,3,5,4])

a,b=least_square(x,y)
print ("Least square method")
print (a,b)