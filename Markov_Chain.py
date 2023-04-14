import random


transition_probabilities = {
    'sunny': {'sunny': 0.8, 'rainy': 0.2},
    'rainy': {'sunny': 0.4, 'rainy': 0.6}
}


current_state = 'rainy'


for i in range(5):
    print(current_state)
    next_states = list(transition_probabilities[current_state].keys())
    probabilities = list(transition_probabilities[current_state].values())
    current_state = random.choices(next_states, probabilities)[0]