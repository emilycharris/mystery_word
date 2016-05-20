import random


def draw_word_spaces():
     if letter in good_guesses:
         print(letter + " ", end='')
     else:
         print('_ ', end='')


def get_secret_word():
    with open("words") as opened_file:
        words = opened_file.read().split("\n")
        global secret_word
        secret_word = random.choice(words).lower()
        print(secret_word)
        global secret_word_letters
        secret_word_letters = list(secret_word)

#The computer must select a word at random from the list of words in the file
get_secret_word()

#Let the user know how many letters the computer's word contains.

print("The secret word contains " + str(len(secret_word)) + " letters.")


#Ask the user to supply one guess (i.e. letter) per round.
#This letter can be upper or lower case and it should not matter.

guess = input("Guess a letter: ").lower()
bad_guesses = []
good_guesses = []

#If they guess a letter that is in the computer's word, they do not lose a guess.
#Let the user know if their guess appears in the computer's word.
#Display the partially guessed word, as well as letters that have not been guessed.
#A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
#A user loses a guess only when they guess incorrectly.


while len(bad_guesses) < 7:
    for letter in secret_word_letters:
        if guess in secret_word_letters:
            if guess not in good_guesses:
                good_guesses.append(guess)
                print("That's right")
            draw_word_spaces()
        else:
            if guess not in bad_guesses:
                bad_guesses.append(guess)

                for letter in secret_word_letters:
                    draw_word_spaces()


    #print("\n"+"Good guesses: " + str(good_guesses))
    #print("Bad guesses: " + str(bad_guesses))
    guess = input("\n"+"You have {} guesses left. Guess again: ".format(8-len(bad_guesses))).lower()
else:
    print("\n" + "Sorry, you're out of turns.  The word was {}.".format(secret_word))


    #If the user guesses the same letter twice, do not take away a guess.
    #Instead, print a message letting them know they've already guessed that letter and ask them to try again.
    #The game should end when the user constructs the full word or runs out of guesses.
    #If the player runs out of guesses, reveal the word to the user when the game ends.
