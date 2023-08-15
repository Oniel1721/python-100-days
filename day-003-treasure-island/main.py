treasure_beauty_print = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''
print(treasure_beauty_print)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
quiz_schema = {
    'title': 'You\'re at a cross road. Where do you want to go? Type "left" or "right"',
    'choices': {
        'left': {
            'title': 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.',
            'choices': {
                'wait': {
                    'title': "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?",
                    'choices': {
                        'red': {
                            'title': "It's a room full of fire. Game Over."
                        },
                        'yellow': {
                            'title': "You found the treasure! You Win!"
                        },
                        'blue': {
                            'title': "You enter a room of beasts. Game Over."
                        },
                    },
                    'default': "You chose a door that doesn't exist. Game Over."
                }
            },
            'default': "You get attacked by an angry trout. Game Over."
        }
    },
    'default': 'You fell into a hole. Game Over.'
}

def display_quiz(question: dict):
    title = question.get('title')
    default = question.get('default')
    choices = question.get('choices')
    if title is None: return
    print(title)
    if choices is None: return
    choice = choices.get(input())
    if choice is None:
        print(default)
        return
    display_quiz(choice)

display_quiz(quiz_schema)
