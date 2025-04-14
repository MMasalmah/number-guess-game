import random

class GuessGame:
    def __init__(self, lower_limit=1, upper_limit=100):
        if lower_limit >= upper_limit:
            raise ValueError("Lower limit must be less than upper limit.")
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit
        self._random_number = random.randint(lower_limit, upper_limit)

    def _get_valid_guess(self) -> int:
        while True:
            try:
                guess = int(input(f"Enter your guess ({self._lower_limit}-{self._upper_limit}): "))
                if self._is_guess_in_range(guess):
                    return guess
                else:
                    print(f"Your guess is out of bounds! Please enter between {self._lower_limit} and {self._upper_limit}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _is_guess_in_range(self, guess: int) -> bool:
        return self._lower_limit <= guess <= self._upper_limit

    def _is_correct_guess(self, guess: int) -> bool:
        return guess == self._random_number

    def _give_hint(self, guess: int) -> None:
        if guess < self._random_number:
            print("Try Higher!")
        elif guess > self._random_number:
            print("Try Lower!")

    def play_game(self):
        print("Welcome to the Guessing Game!")
        while True:
            guess = self._get_valid_guess()
            if self._is_correct_guess(guess):
                print("Correct! You guessed the number.")
                break
            else:
                self._give_hint(guess)
