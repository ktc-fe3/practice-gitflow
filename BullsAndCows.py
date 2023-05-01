import random
import itertools


def createRandom():
    randomList = [''.join(x) for x in list(itertools.permutations('0123456789',4))]

    return str(random.choice(randomList))


def get_input():
    while True:
        user_input = input("")
        number = len(user_input)
        print(number)
        if user_input.isalpha():
            print("숫자를 입력해주세요.")
            continue
        if number!=4:
            print("4개의 숫자를 입력해주세요")
            continue

        else:
            break
    return user_input


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


def getScore(code,guess):
    Bulls = 0
    Cows = 0
    (Bulls,Cows) = count_bulls_cows(code,guess)

    print("Bulls:",Bulls," Cows:",Cows)


answer = createRandom()

count = 0
while True:
    count += 1
    input_numbers = get_input()
    getScore(answer, input_numbers)

    if answer == input_numbers:
        print(f"{count} 번 시도 만에 정답을 찾았습니다.")
        break

    print("Bulls:",Bulls," Cows:",Cows)

