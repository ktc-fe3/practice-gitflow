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

inputTest = get_input()
print(inputTest)