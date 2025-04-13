import random

from django.template.defaultfilters import lower


class GuessGame:
    def __init__(self, lower = 1, upper = 100):
        self.lower = lower
        self.upper = upper
        self.random_number = random.randint(lower, upper)


    def get_user_input(self):
        try:
            guess = int(input(f"Please enter a guess (between {self.lower} and {self.upper}): "))
            return guess
        except ValueError:
            print("Please enter an integer!")
            return None

    def ckech_bound(self, guess):
        return self.lower <= guess <= self.upper

    def compare_guess(self, guess):
        if guess > self.random_number:
            return "Lower!"
        elif guess < self.random_number:
            return "Higher!"
        else:
            return "Equal"

    def play_game(self):
        print("Game started !!")
        while True:
            guess = self.get_user_input()
            if guess is None:
                continue

            if not self.ckech_bound(guess):
                print("Out of range. Try again.")
                continue

            result = self.compare_guess(guess)
            print(result)

            if result == "Equal":
                print("You guessed it!")
                break






