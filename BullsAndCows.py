
# count bulls and cows
def count_bulls_cows(code, guess):
    bulls = cows = 0
    for i, digit in enumerate(guess):
        print(i,digit)
        if digit == code[i]:
            bulls += 1
        elif digit in code:
            cows += 1
    return bulls, cows

import random
import itertools

def createRandom():
    randomList = [''.join(x) for x in list(itertools.permutations('0123456789',4))]
    return int(random.choice(randomList))
