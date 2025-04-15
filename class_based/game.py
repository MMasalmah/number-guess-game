import random

class GuessGame:
    def __init__(self, lower_limit=1, upper_limit=100):
        if lower_limit >= upper_limit:
            raise ValueError("Lower limit must be less than upper limit.")
        self.__lower_limit = lower_limit
        self.__upper_limit = upper_limit
        self.__random_number = random.randint(lower_limit, upper_limit)

    def _get_guess(self) -> str:
        return input(f"Enter your guess ({self.__lower_limit}-{self.__upper_limit}): ")

    def is_guess_in_range(self, guess: int) -> bool:
        return self.__lower_limit <= guess <= self.__upper_limit

    def get_range_error_message(self, guess: int) -> str:
        return f"Your guess ({guess}) is out of bounds! Please enter between {self.__lower_limit} and {self.__upper_limit}."

    def is_correct_guess(self, guess: int) -> bool:
        return guess == self.__random_number

    def give_hint(self, guess: int) -> str:
        if guess < self.__random_number:
            return "Try Higher!"
        elif guess > self.__random_number:
            return "Try Lower!"
        return ""

    def get_success_message(self) -> str:
        return f"Correct! You guessed the number {self.__random_number}."

    def check_guess_validity(self, guess_str: str) -> int:
        try:
            guess = int(guess_str)
        except ValueError:
            raise ValueError("Invalid input. Please enter a number.")

        if not self.is_guess_in_range(guess):
            raise ValueError(self.get_range_error_message(guess))

        return guess

    def play_game(self):
        print("Welcome to the Guessing Game!")
        while True:
            guess = self._get_guess()
            try:
                guess = self.check_guess_validity(guess)
            except ValueError as e:
                print(e)
                continue

            if self.is_correct_guess(guess):
                print(self.get_success_message())
                break
            else:
                print(self.give_hint(guess))
