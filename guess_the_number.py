import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    # while True loop with try and except blocks used for input validation
    while True:
        try:
            guess = int(input('Guess the secret number? '))
            break  # end while loop - we got an integer - no exception was raised
        except ValueError:  # handles user entering non-integer guess
            print("That was not an integer number. Please try again.")
            # while True loop repeats after exception is raised
    return guess


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high) #

    counter = 0   # This is going to track the number of guesses

    while True:

        counter += 1   # increment for counter
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print(f'Thanks for playing the game! The number of guesses it took {counter}')


if __name__ == '__main__':
    main()
