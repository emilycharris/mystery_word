import random
import sys

blanks = 0
turns = 0
bad_guesses = []
good_guesses = []

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
        global secret_word_letters
        secret_word_letters = list(secret_word)
        print("The secret word contains " + str(len(secret_word)) + " letters.")


def game_loop():
    turns = 0
    while True:
        for _ in secret_word:
            draw_word_spaces()
            guess = input("\n\nYou have {} turns left. \nGuess a letter: ".format(8-turns)).lower()
            if guess in good_guesses or guess in bad_guesses:
                print("You've already guessed that letter.  Try again.\n")
            elif guess in secret_word:
                if guess not in good_guesses:
                    good_guesses.append(guess)
                    print("\nThat's right! You keep all your turns.")
            else:
                turns += 1
                if guess not in bad_guesses:
                    bad_guesses.append(guess)
                    print("\nNo, that letter's not included.")
                    print("You've taken {} of 8 turns. ".format(turns))
                    if turns > 7:
                        print("\nSorry, you're out of turns.  The word was {}.".format(secret_word))
                        return False

def game():
    get_secret_word()
    game_loop()

game()