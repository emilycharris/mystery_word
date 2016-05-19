

def get_guess(bad_guesses, good_guesses):

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in good_guesses or guess in bad_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print('You can only guess letters!')
        else:
            return guess
