import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def chooseDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input. Please try again.")
        chooseDifficulty()

attempts = chooseDifficulty()
number = random.randint(1, 100)

def guessNumber():
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    clear()
    if guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    return False

while attempts > 0:
    if guessNumber():
        break
    attempts -= 1