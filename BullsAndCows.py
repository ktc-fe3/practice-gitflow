import random
import itertools

def createRandom():
    randomList = [''.join(x) for x in list(itertools.permutations('0123456789',4))]
    return random.choice(randomList)

print(createRandom())