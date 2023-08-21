import random
import os

words = ["apple", "banana", "orange", "coconut", "strawberry", "lime", "grapefruit", "lemon", "kumquat", "blueberry", "melon", "united states", "canada", "mexico", "brazil", "argentina", "chile", "peru", "colombia", "venezuela", "ecuador", "bolivia", "paraguay", "uruguay", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "brown", "gray", "purple", "pink"]

word = random.choice(words)
word_length = len(word)
guessed_letters = []
lives = 6

def print_hangman(lives):
    head = "O" if lives < 6 else " "
    body = "|" if lives < 5 else " "
    left_arm = "/" if lives < 4 else " "
    right_arm = "\\" if lives < 3 else " "
    left_leg = "/" if lives < 2 else " "
    right_leg = "\\" if lives < 1 else " "
    print("  _______")
    print("  |     |")
    print(f"  |     {head}")
    print(f"  |    {left_arm}{body}{right_arm}")
    print(f"  |    {left_leg} {right_leg}")
    print("  |")
    print("  |")
    print("__|__")

def print_word():
    result = ""
    for right_letter in word:
        if right_letter in guessed_letters:
            result += right_letter
        else:
            result += "_"
    print("  "+ result)

def hasWin():
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

while lives > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    if hasWin():
        break
    print_hangman(lives)
    print_word()
    letter = input("Guess a letter: ").lower()
    if letter in word:
        guessed_letters.append(letter)
    else:
        lives -=1
    

if lives > 0:
    print_word()
    print("Congratulations you won!!!")
else:
    print_hangman(lives)
    print("I'm sorry you lose")

    
