def getScore(code,guess):
    Bulls = 0
    Cows = 0
    (Bulls,Cows) = count_bulls_cows(code,guess)

    print("Bulls:",Bulls," Cows:",Cows)