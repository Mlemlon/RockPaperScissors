from random import randint
opcje = ["Rock", "Paper", "Scissors"]

computer = opcje[randint(0,2)]

player = False  

while player == False:
    player = input("Rock, paper or scissors: ")
    if player == computer:
        print("Tie! ")
    elif player == "Rock":
        if computer == "Paper":
            print("You Loose !", player ," vs ", computer)
        else:
            print("You win! ", player, "vs", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose ", player, " vs ", computer)
        else:
            print("You win! ", player, " vs ", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose! ", player, " vs ", computer)
        else:
            print("you Win! ", player, " vs ", computer)
    else:
        print("not a valid play")

player = False

computer = opcje[randint(0,2)]
