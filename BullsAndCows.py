import random
import itertools

def createRandom():
    randomList = [''.join(x) for x in list(itertools.permutations('0123456789',4))]
    return int(random.choice(randomList))

