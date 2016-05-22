#turns are iterating correctly through the += 1 command.
#"While turns < 8" loop isn't working correctly every time.

import random
import sys

bad_guesses = []
good_guesses = []
easy_list = []
medium_list = []
hard_list = []

blanks = 0
turns = 0


def get_secret_word():
    with open("words") as opened_file:
        words = opened_file.read().split("\n")
        for word in words:
            if len(word) >= 4 and len(word) < 6:
                easy_list.append(word)
            elif len(word) >= 6 and len(word) < 10:
                medium_list.append(word)
            elif len(word) >= 10:
                hard_list.append(word)

    global difficulty_input
    global secret_word
    difficulty_input = input("Select your level of difficulty: (E)asy, (M)edium, or (H)ard: \n").lower()
    if difficulty_input == "e" or difficulty_input == "easy":
        secret_word = random.choice(easy_list).lower()
    elif difficulty_input == "m" or difficulty_input == "medium":
        secret_word = random.choice(medium_list).lower()
    elif difficulty_input == "h" or difficulty_input == "hard":
        secret_word = random.choice(hard_list).lower()
    else:
        new_game()
    print("The secret word contains " + str(len(secret_word)) + " letters.\n")


def game_loop():
    turns = 0
    while True:
        for _ in secret_word:
            draw_word_spaces()
            guess = input("\n\nYou have {} turns left. \nGuess a letter: ".format(8-turns)).lower()
            if len(guess) != 1:
                print("Make sure you guess one letter.\n")
            elif guess in good_guesses or guess in bad_guesses:
                print("You've already guessed that letter.  Try again.\n")
            elif guess in secret_word:
                turns += 0
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
                        clear()
                        new_game()


def clear():
    del good_guesses[:]
    del bad_guesses[:]
    turns = 0


def draw_word_spaces():
    blanks = 0
    global letter
    for letter in secret_word:
        if letter in good_guesses:
            print(letter + " ", end='')
        else:
            print('_ ', end='')
            blanks += 1
    if blanks == 0 and (len(good_guesses) > 0 or len(bad_guesses) > 0):
        print("\n"+"You win")
        new_game()


def new_game():
    global start_over
    start_over = input("Do you want to play again? (Y)es/(N)o: \n").lower()
    if start_over == "y" or start_over == "yes":
        clear()
        game()
    elif start_over == "n" or start_over == "no":
        sys.exit()
    else:
        new_game()


def game():
    get_secret_word()
    game_loop()
    clear()


game()
