import random
import sys

blanks = 0
def draw_word_spaces():
    blanks = 0
    for letter in secret_word:
        if letter in good_guesses:
            print(letter + " ", end='')
        else:
            print('_ ', end='')
            blanks += 1
    if blanks == 0 and (len(good_guesses) > 0 or len(bad_guesses) > 0):
        print("\n"+"You win")
        sys.exit()

def get_secret_word():
    with open("words") as opened_file:
        words = opened_file.read().split("\n")
        global secret_word
        secret_word = random.choice(words).lower()
        print(secret_word)
        global secret_word_letters
        secret_word_letters = list(secret_word)

def duplicate_guess():
    if guess in good_guesses or guess in bad_guesses:
        print("I'm sorry, that letter has already been used")


get_secret_word()

print("The secret word contains " + str(len(secret_word)) + " letters.")

guess = input("Guess a letter: ").lower()
bad_guesses = []
good_guesses = []


while len(bad_guesses) < 7:
    duplicate_guess()
    for letter in secret_word_letters:
        if guess in secret_word_letters:
            if guess not in good_guesses:
                good_guesses.append(guess)
                print("\n" + "That's right")
        else:
            if guess not in bad_guesses:
                bad_guesses.append(guess)

    draw_word_spaces()

    guess = input("\n"+"You have {} guesses left. Guess again: ".format(8-len(bad_guesses))).lower()
else:
    print("\n" + "Sorry, you're out of turns.  The word was {}.".format(secret_word))
