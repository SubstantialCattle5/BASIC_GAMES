'''
########################################################

 Acey Ducey

From: BASIC Computer Games (1978)
      Edited by David Ahl

This is a simulation of the Acey Ducey card game.
  In the game, the dealer (the computer) deals two
  cards face up.  You have an option to bet or not to
  bet depending on whether you feel the next
  card dealt will have a value between the first two.

 Your initial money is set to $100. The game keeps
  going on until you lose all your money or interrupt
  the program.

 "The original BASIC program author was Bill Palmby
  of Prairie View, Illinois."

########################################################
'''

import random

cards = {
    0: '1',
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "Jack",
    11: "Queen",
    12: "King",
    13: "Ace",
}

# You may alter initial_money if you want to start with more or less than $100
initial_money = 100


def face_up():
    a, b = cards[random.randint(1, 14)], cards[random.randint(1, 14)]
    if a == b:
        face_up()
    else:
        return a, b


while initial_money >= 0:
    # Display initial title and instructions
    print("\n\t\tAcey Ducey Card Game")
    print("Creative Computing  Morristown, New Jersey")
    print("\n\n")
    print("Acey-Ducey is played in the following manner")
    print("The dealer (computer) deals two cards face up")
    print("You have an option to bet or not bet depending")
    print("on whether or not you feel the card will have")
    print("a value between the first two.")
    print("If you do not want to bet, input a 0")
    print(f'You have {initial_money} DOLLARS\n')

    # initializing the card
    A, B = face_up()
    M = int(input('What is your BET?'))
    if M == 0:
        print("CHICKEN!!!!!!!!\n")
        break
    else:
        print(f'Here are your next two cards\n{A}\n{B}')
        if M>initial_money :
            print(f'Sorry, My friend but you bet too much\nYou only have {initial_money} dollars left to bet')
            continue
        C = cards[random.randint(1, 14)]



    break
