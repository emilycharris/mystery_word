import random
import sys

#choose level of difficulty
    #easy = 4-6 characters
    #normal = 6-10 characters
    #hard = 10+ characters
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
        global secret_word
        secret_word = random.choice(words).lower()
        print(secret_word)
        global secret_word_letters
        secret_word_letters = list(secret_word)
        print("The secret word contains " + str(len(secret_word)) + " letters.")

#def guess_error_checking():
    #guess = input("Guess a letter: \n").lower()

    #if guess in good_guesses or guess in bad_guesses:
        #print("I'm sorry, that letter has already been used.  Try again. \n")

    #elif len(guess) != 1:
        #print("Make sure you're only guessing one letter! Try again. \n")

    #else:
        #pass


get_secret_word()

bad_guesses = []
good_guesses = []

blanks = 0



while len(bad_guesses) < 7:
    for letter in secret_word_letters:
        guess = input("\n"+"You have {} guesses left. Guess a letter: \n".format(8-len(bad_guesses))).lower()
        if len(guess) != 1:
            print("Make sure you guess one letter.")
        elif guess in good_guesses or guess in bad_guesses:
            print("You've already guessed that letter.  Try again.")
        elif guess in secret_word_letters:
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