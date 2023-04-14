import numpy as np
def sphereman_corr(x,y):
  x_rank = np.argsort(x).argsort()
  y_rank = np.argsort(y).argsort()
  d_rank=x_rank-y_rank
  d_rank_square=np.square(d_rank)
  n=len(x)
  r = 1-(6*np.sum(d_rank_square))/(n*(n**2-1))
  return r
x_data=[56,75,45,71]
y_data=[66,70,40,60]
r=sphereman_corr(x_data,y_data)
print ("sphereman method")
print (r)