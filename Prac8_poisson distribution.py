import math

# Average number of homes sold per day
lam = 2

# Number of homes sold tomorrow
k = 3

# Probability of selling k homes tomorrow
prob = (lam ** k) * math.exp(-lam) / math.factorial(k)

print("Probability of selling exactly 3 homes tomorrow:", prob)