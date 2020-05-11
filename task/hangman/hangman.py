import random
import string


def letters_in_word(word):
    return set(word)


def show_letters(letter):
    global correct
    global hint
    new = ''
    for j in range(len(correct)):
        if letter == correct[j]:
            new += letter
        else:
            new += hint[j]
    return new


def play():

    global correct
    letters = letters_in_word(correct)
    global hint
    used = []
    ascii_lowercase = string.ascii_lowercase
    max_tries = 8
    tries = 0
    for i in range(len(correct)):
        hint.append('-')
    hint = ''.join(hint)

    while tries < max_tries:
        print('\n')
        print(hint)
        letter = input("Input a letter: ")
        if hint == correct:
            break
        if len(letter) != 1:
            print("You should print a single letter")
            continue
        if letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue
        if letter in letters:
            if letter in used:
                print("You already typed this letter")
            else:
                hint = show_letters(letter)
                used.append(letter)
        else:
            if letter in used:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                used.append(letter)
                tries += 1

    if tries < max_tries:
        print("You survived!")
    else:
        print("You are hanged!")


print("H A N G M A N")
while True:
    possible = ['python', 'java', 'kotlin', 'javascript']
    correct = random.choice(possible)
    hint = []
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        play()
    elif choice == 'exit':
        break
    else:
        continue
