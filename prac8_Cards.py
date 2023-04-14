import math
N = 52
n_hearts = 13
n_drawn = 5
n_ways = 0
for k in range(3):
    n_ways += math.comb(n_hearts, k) * math.comb(N - n_hearts, n_drawn - k)
n_total_ways = math.comb(N, n_drawn)
prob = n_ways / n_total_ways
print("Probability of obtaining 2 or fewer hearts:", prob)
N = 52
n_spades = 1
n_hearts = 1
n_diamonds = 1
n_clubs = 2
n_drawn = n_spades + n_hearts + n_diamonds + n_clubs
p_spade = 1 / 4
p_heart = 1 / 4
p_diamond = 1 / 4
p_club = 1 / 4
prob = (p_spade * n_spades) * (p_heart * n_hearts) * (p_diamond * n_diamonds) * (p_club * n_clubs)
print("Probability of drawing 1 spade, 1 heart, 1 diamond, and 2 clubs:", prob)