import random


def game():
    while True:
        random_num = random.randint(1, 100)
        guess = int(input("Enter a number: "))

        if guess > random_num:
            print(f"higher than {random_num}")
        elif guess < random_num:
            print(f"lower than {random_num}")
        else:
            print("equal")
            break


#start the game
game()
