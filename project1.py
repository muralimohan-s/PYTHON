# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:36:10 2021

@author: MuraliMohan s

"""

import random


game_list = ["stone", "paper", "scissors"]
game_list_quit = ["stone", "paper", "scissors", "quit"]
computer_score = 0
player_score = 0
print("score:computer = {x}  score:player = {y}".format(x=computer_score, y=player_score))

while True:
    computer_choice = random.choice(game_list)
    print("\n",game_list)
    command = input("please select your choice from the list\n")
    if command in game_list_quit:
        if command == computer_choice:
            print("Tie")
        elif command == "stone":
            if computer_choice == "scissors":
                print("player won!")
                player_score += 1
            else:
                print("computer won!")
                computer_score += 1
        elif command == "paper":
            if computer_choice == "stone":
                print ("Player won!")
                player_score += 1
            else:
                print("computer won!")
                computer_score += 1
        elif command == "scissors":
            if computer_choice == "paper":
                print("player won!")
                player_score += 1
            else:
                print("computer won!")
                computer_score += 1
        elif command == "quit":
            if player_score > computer_score:
                print("player won the game, player score:{x}, computer score:{y}".format(x=str(player_score), y=str(computer_score)))
                break
            elif computer_score > player_score:
                print("computer won the game, player score:{x}, computer score:{y}".format(x=str(player_score), y=str(computer_score)))
                break
            else:
                print("tie, player score:{x}, computer score:{y}".format(x=str(player_score), y=str(computer_score)))
                break
    else:
        print("invalid command")
