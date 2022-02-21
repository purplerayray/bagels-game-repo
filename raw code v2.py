import random

# NUM_DIGITS = 3
# MAX_GUESSES = 10

def game_setting():
    NUM_DIGITS = int(input("Enter Digits > "))
    MAX_GUESSES = NUM_DIGITS * 4
    print("{} Digits\n{} guesses".format(NUM_DIGITS, MAX_GUESSES))
    return NUM_DIGITS, MAX_GUESSES

def get_secret_num(NUM_DIGITS):
    num_list = list('0123456789')
    numbers = []
    random.shuffle(num_list)
    for i in range(NUM_DIGITS):
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

def main_code(NUM_DIGITS, MAX_GUESSES):
    while True:
        secret_num = get_secret_num(NUM_DIGITS)
        print('I have thought of a {} digit number'.format(NUM_DIGITS))
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        tries = 1
        while tries <= MAX_GUESSES:
            print('\nGuess #{}: '.format(tries))
            guess = input('> ')
            if guess == secret_num:
                print('That\'s right!')
                break
            else:
                print(clues_generator(guess, secret_num))
                tries += 1
        if tries > MAX_GUESSES:
            print('\nYou\'re out of guesses.')
            print('The answer was {}.'.format(secret_num))

        option = input('\nDo you want to play again? (y/n) \n> ')
        if option == 'n':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    digit, guess = game_setting()
    main_code(digit, guess)