import random

numbers = list(range(1, 101))
random_number = random.choice(numbers)

user_guess = int(input("Guess a number between 1 and 100: "))
    
if user_guess == random_number:
        print("Good job! You guessed it right.")
else:
        print("Try again! The correct number was:", random_number)