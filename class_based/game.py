import random

def range_checker(lower, upper):
    def check(guess):
        return lower <= guess <= upper
    return check

class GuessGame:
    def __init__(self, lower_limit=1, upper_limit=100):
        if lower_limit >= upper_limit:
            raise ValueError("Lower limit must be less than upper limit.")
        self.__lower_limit = lower_limit
        self.__upper_limit = upper_limit
        self.__random_number = random.randint(lower_limit, upper_limit)
        self.__is_in_range = range_checker(lower_limit, upper_limit)

    def __get_guess(self) -> str:
        return input(f"Enter your guess ({self.__lower_limit}-{self.__upper_limit}): ")

    def __check_guess_validity(self, guess_str: str) -> int:
        try:
            guess = int(guess_str)
        except ValueError:
            raise ValueError("Invalid input. Please enter a number.")

        if not self.__is_in_range(guess):
            raise ValueError(f"Your guess ({guess}) is out of bounds! Please enter between {self.__lower_limit} and {self.__upper_limit}.")

        return guess

    def __give_hint(self, guess: int) -> str:
        if guess < self.__random_number:
            return "Try Higher!"
        elif guess > self.__random_number:
            return "Try Lower!"
        return ""

    def __get_success_message(self) -> str:
        return f"Correct! You guessed the number {self.__random_number}."

    def play_game(self):
        print("Welcome to the Guessing Game!")
        while True:
            guess = self.__get_guess()
            try:
                guess = self.__check_guess_validity(guess)
            except ValueError as e:
                print(e)
                continue

            if guess == self.__random_number:
                print(self.__get_success_message())
                break
            else:
                print(self.__give_hint(guess))
