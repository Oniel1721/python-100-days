import random
rock = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissors = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

choices = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
try:
    choice_index = int(input())
    player_choice = choices[choice_index]
    pc_choice = choices[random.randint(0,2)]
    print(player_choice+"\n")
    print("Computer chose:\n")
    print(pc_choice+"\n") 
    if player_choice == pc_choice:
        print("It's a draw")
    elif (player_choice == rock and pc_choice == scissors) or (player_choice == paper and pc_choice == rock) or (player_choice == scissors and pc_choice == paper):
        print("You win!")
    else:
        print("You lose")
except:
    print("Invalid Option")
