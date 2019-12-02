while True:
    import random
    chars = 'abcdefghijklmnopqrstuvwxyz12345678910!@#$%^&*'
    number = input('How many passwords would you like to generate?')
    number = int(number)
    length = input('How long would you like your passwords?')
    length = int(length)
    for p in range (number):
        password = ''
        for c in range (length):
            password += random.choice(chars)
        print(password)
    while True:
        answer = input('Would you like to generate more passwords?')
        if answer in ('y','yes','Yes','n','no','No'):
            break
        print('Invalid input.')
    if answer == 'y' or answer == 'yes' or answer == 'Yes':
        continue
    else: print ('Goodbye!')
    break

