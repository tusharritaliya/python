import random

number = random.randint(1, 50)

guess = int(input("Guess a number (1-50): "))

if guess == number:
    print("Correct Guess!")
else:
    print("Wrong! Number was:", number)