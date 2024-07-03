

while True:
    user_input = int(input('When was Python 1.0 released? '))
    if user_input < 1994:
        print('It was later than that!')
    elif user_input > 1994:
        print('It was earlier than that!')
    else:
        print('Correct!')
        break