import random


GAME_RULES = "What number is missing in the progression?"


def generate_geometric_progression(length):
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    return progression


def generate_round():
    length = random.randint(5, 10)
    progression = generate_geometric_progression(length)
    missing_index = random.randint(0, length - 1)
    missing_value = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, missing_value
