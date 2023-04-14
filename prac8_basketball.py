import math

# Probability of making a free throw
p = 0.7
# Number of free throws attempted
n = 5

comb = math.comb(n-1, 2)
prob = comb * (p * 3) * ((1 - p) * 2)
print("Probability of making the third free throw on the fifth shot:", prob)