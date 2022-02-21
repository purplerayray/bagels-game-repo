import random

def get_secret_num(num_digits):
    num_list = list('0123456789')
    numbers = []
    random.shuffle(num_list)
    for i in range(num_digits):
        numbers.append(num_list[i])
    secret_num = "".join(str(x) for x in numbers)
    return secret_num

def clues_generator(guess, secret_num):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if clues:
        clues.sort()
        return ' '.join(clues)
    else:
        return 'Bagels'

def check_guess(guess, secret_num):
    if guess == secret_num:
        return True
    else:
        return False
