import random


class GuessGame:
    def __init__(self, lower = 1, upper = 100):
        self.lower = lower
        self.upper = upper

    def get_user_input(self):
        guess = int(input("Hello Dear,\n Please enter a guess (between 1 and 100): "))
        return guess

    def play_game(self):
        while True:

            random_num = random.randint(1, 100)
            guess = self.get_user_input()

            if guess > self.upper or guess < self.lower :
                print("Unvalid Input, Please try again with valid input")
                continue

            if guess > random_num:
                print(f"higher! the random number is {random_num}")
            elif guess < random_num:
                print(f"lower! the random number is {random_num}")
            else:
                print("Equal, congrats")
                break


