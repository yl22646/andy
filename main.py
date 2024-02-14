import random
import easygui

player_score = 0
npc_score = 0
play = 0
npc_choice = 0

def npc():
    npc = ["Rock", "Paper", "Scissors"]
    npc_choice = random.choice(npc)
    if npc_choice == "rock":
        npc_choice = 2
    
    elif npc_choice == "paper":
        npc_choice = 3
    
    else:
        npc_choice = 1


def player_choice():
    play = input("pick rock paper or scissors\n")
    if play == "rock":
        play = 1
    
    elif play == "paper":
        play = 2
    
    else:
        play = 3

while player_score or npc_score < 5:
    npc()
    player_choice()
    
    if play > npc_choice:
        print(f"you win, player{player_score} - npc{npc_score}")
        player_score += 1
    
    elif play == npc_choice:
        print(f"you lose, player{player_score} - npc{npc_score}")
        npc_score += 1

    else:
        print(f"draw, player{player_score} - npc{npc_score}")

if player_score == 5:
    print("good job you win")

elif npc_score == 5:
    print("unlucky u lose")





