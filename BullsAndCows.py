def get_input():
    while True:
        user_input = input("숫자를 입력하세요")
        number = user_input.split()
        if user_input.isalpha():
            continue
        else:
            break
    return user_input

inputTest = get_input()
print(inputTest)