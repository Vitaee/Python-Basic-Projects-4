# -*- coding: utf-8 -*-
""" 
"""
import random

# Tic-Tac-Toe game

def printBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j],end=" ")
        print("")

def Check_WIN(Player,Board):
    # Check Rows
    for Row in [0,1,2]:
        if Board[Row][0]!='-' and Board[Row][0]== Board[Row][1] and Board[Row][1]==Board[Row][2]:
            WIN=True
            return(WIN)

    # Check Columns
    for Col in [0,1,2]:
        if Board[0][Col]!='-' and Board[0][Col]== Board[1][Col] and Board[1][Col]==Board[2][Col]:
            WIN=True
            return(WIN)


    # Check Diagonals
    if Board[0][0]!='-' and Board[0][0]== Board[1][1] and Board[1][1]==Board[2][2]:
        WIN=True
        return(WIN)


    if Board[0][2]!='-' and Board[0][2]== Board[1][1] and Board[1][1]==Board[2][0]:
        WIN=True
        return(WIN)

    WIN=False
    return(WIN)

# Iniatial Board Cofıguration
Board=[["-","-","-"],["-","-","-"],["-","-","-"]]
printBoard(Board)

WIN=False
print("Determning the turn of players randomly")
if random.random() <= 0.5:
    TURN=0  # Player X
else:
    TURN=1  # Player O

Num_Moves=0

while not WIN and Num_Moves <9:
    if TURN==0:
        print("Its  the PLAYER X's TURN:")
        TURN = 1
        Row,Col= [int(x) for x in input("Enter Row-Column indexes of your tile (space separated): ").split()]
        Board[Row-1][Col-1]="X"
        printBoard(Board)
        Num_Moves +=1
        if Num_Moves > 4:
            WIN=Check_WIN(TURN,Board)
            if WIN:
                print("CONGRATULATION PLAYER X: YOU WIN THE GAME")
                break
    else:
        print("It's the PLAYER O's TURN")
        TURN=0
        Row,Col= [int(x) for x in input("Enter Row-Column indexes of your tile (space separated): ").split()]
        Board[Row-1][Col-1]="O"
        printBoard(Board)
        Num_Moves += 1
        if Num_Moves > 4:
            WIN=Check_WIN(TURN,Board)
            if WIN:
                print("CONGRATULATION PLAYER O: YOU WIN THE GAME")
                break

if Num_Moves == 9:
    print("CONGRATULATIONS TO BOTH PLAYERS")
    print("Game Ended with a TIE score")
