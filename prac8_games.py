import math

# Probability of winning a single game
p = 0.5

# Number of games in the series
n = 7

# Probability of World Series lasting i games
for i in range(4, n+1):
    # Calculate probability of i games being played
    comb = math.comb(n, i)
    prob_i = comb * (p * i) * ((1 - p) * (n - i))
    print("Probability of World Series lasting", i, "games:", prob_i)