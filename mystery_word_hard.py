import random
import sys


bad_guesses = []
good_guesses = []
easy_list = []
medium_list = []
hard_list = []

blanks = 0
#add loop to restart game

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
    if difficulty_input == "m" or difficulty_input == "medium":
        secret_word = random.choice(medium_list).lower()
    if difficulty_input == "h" or difficulty_input == "hard":
        secret_word = random.choice(hard_list).lower()
    print("The secret word contains " + str(len(secret_word)) + " letters.")

get_secret_word()

while len(bad_guesses) < 7:
    for letter in secret_word:
        guess = input("\n"+"You have {} guesses left. Guess a letter: \n".format(8-len(bad_guesses))).lower()
        if len(guess) != 1:
            print("Make sure you guess one letter.")
        elif guess in good_guesses or guess in bad_guesses:
            print("You've already guessed that letter.  Try again.")
        elif guess in secret_word:
            if guess not in good_guesses:
                good_guesses.append(guess)
                print("\n" + "That's right!")
                draw_word_spaces()
        else:
            if guess not in bad_guesses:
                bad_guesses.append(guess)
                print("\n" + "No, that letter's not included.")
                draw_word_spaces()

else:
    print("\n" + "Sorry, you're out of turns.  The word was {}.".format(secret_word))