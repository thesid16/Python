import random

def get_choices():
    player_Choice = input ("Entere a choise (rock, Paper, scissors ):  ")
    options = ["rock", "paper", "scissors"]
    Computer_Choise = random.choice(options)
    
    choices = {"player": player_Choice, "computer": Computer_Choise}
    return choices

def check_win(player,computer):
    print("You Choose: " + player + " Computer Choose : " + computer)
    if player == computer:
        return "It's a tie"
    
