import random
import sys

bad_guesses = []
good_guesses = []
word_list = []

blanks = 0
turns = 0


def get_secret_word():
    with open("words") as opened_file:
        words = opened_file.read().split("\n")
        words.sort(key=lambda x: len(x))

        if len(words[0]) == 0:
            minimum = 1
        else:
            minimum = len(words[0])

        maximum = len(words[-1])

        global word
        global word_length
        global secret_word

        try:
            word_length = int(input("Pick a number between {} and {}.".format(minimum, maximum)))
        except ValueError:
            new_game()

        for word in words:
            if word_length < minimum or word_length > maximum:
                print("That number isn't within the range. ")
            else:
                if len(word) == word_length:
                    word_list.append(word)

        secret_word = random.choice(word_list).lower()
        print(secret_word)


def game_loop():
    turns_taken = 0
    selected_turns = int(input("How many guesses would you like? "))
    if selected_turns <= 0:
        print("Please select a number greater than zero. ")
        new_game()

    while True:
        for _ in secret_word:
            draw_word_spaces()
            guess = input("\n\nYou have {} turns left. \nGuess a letter: ".format(selected_turns-turns_taken)).lower()
            if len(guess) != 1:
                print("Make sure you guess one letter.\n")
            elif guess in good_guesses or guess in bad_guesses:
                print("You've already guessed that letter.  Try again.\n")
            elif guess in secret_word:
                turns_taken += 0
                if guess not in good_guesses:
                    good_guesses.append(guess)
                    print("\nThat's right! You keep all your turns.")
            else:
                turns_taken += 1
                if guess not in bad_guesses:
                    bad_guesses.append(guess)
                    print("\nNo, that letter's not included.")
                    print("You've taken {} of {} turns. ".format(turns_taken, selected_turns))
                    if turns_taken > selected_turns - 1:
                        print("\nSorry, you're out of turns.  The word was {}.".format(secret_word))
                        return False
                        clear()
                        new_game()


def clear():
    del good_guesses[:]
    del bad_guesses[:]
    del word_list[:]
    turns_taken = 0


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
