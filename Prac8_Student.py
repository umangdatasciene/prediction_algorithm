
import math

# Probability of acceptance
p = 0.3

# Number of trials (students applying)
n = 5

# Probability of at most 2 being accepted
prob = 0
for i in range(3):
    # Calculate probability of i students being accepted
    comb = math.comb(n, i)
    prob_i = comb * (p * i) * ((1 - p) * (n - i))
    prob += prob_i

print("Probability of at most 2 students being accepted:", prob)