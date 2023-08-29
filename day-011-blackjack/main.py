import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wantToPlay():
    return input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower() == 'y'

def wantToGetCard():
    return input('Type "y" to get another card, type "n" to pass: ').lower() == 'y'

def printCards(playerCards, computerCards):
    print(f"Your cards: {playerCards}, current score: {sum(playerCards)}")
    print(f"Computer's first card: {computerCards[0]}")

def printResult(playerCards, computerCards):
    clear()
    print(f"Your final hand: {playerCards}, final score: {sum(playerCards)}")
    print(f"Computer's final hand: {computerCards}, final score: {sum(computerCards)}")

def calculateResults(playerCards, computerCards):
    if sum(playerCards) == 21 and sum(computerCards) == 21:
        printResult(playerCards, computerCards)
        print('Draw!')
        return "Draw"
    if sum(playerCards) == 21 and sum(computerCards) != 21:
        printResult(playerCards, computerCards)
        print('You win!') 
        return "Win"
    elif sum(playerCards) > 21:
        printResult(playerCards, computerCards)
        print('You went over. You lose!')
        return "Lose"
    


while wantToPlay():
    clear()
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random.shuffle(cards)

    playerCards = [cards.pop(), cards.pop()]
    computerCards = [cards.pop(), cards.pop()]
    printCards(playerCards, computerCards)

    if sum(playerCards) != 21:
        while wantToGetCard():
            playerCards.append(cards.pop())
            results = calculateResults(playerCards, computerCards)
            if results == None:
                printCards(playerCards, computerCards)
            else:
                break
    
    results = calculateResults(playerCards, computerCards)
    if results == None:
        printResult(playerCards, computerCards)
        if sum(playerCards) > sum(computerCards):
            print('You win!')
        elif sum(playerCards) < sum(computerCards):
            print('You lose!')
        else:
            print('Draw!')
    

    


    


