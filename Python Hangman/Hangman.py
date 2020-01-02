# -*- coding: utf-8 -*-
"""
"""

#importing functional modules
import random
import time

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Let's play hangman!")

print ("\n")

#wait for 1 second
time.sleep(1)

WordList=["secret", "administration", "level", "secretary", "department"];

print ("Start guessing...")
time.sleep(0.5)

# Select a word randomly form the list
Word = WordList[random.randint(0,len(WordList)-1)]

print(name + ": We play over a word of length of "+str(len(Word)))

# Creates a variable Guess with an empty value
Guess = []
for i in range(len(Word)):
    Guess += '-'

print("Your initial statue is :", Guess)

#determine the number of turns
Max_Num_FalseGuesses = 10
Failed=0

# Create a while loop

#check if the turns are more than zero
while Failed < Max_Num_FalseGuesses:

    # ask the user go guess a character
    Char_Guess = input("Guess a character:")
    if Char_Guess in Guess:
        print("This letter is already tried")
    elif Char_Guess in Word:
        for i in range(len(Word)):
            if Word[i]==Char_Guess:
                Guess[i]=Char_Guess
    else:
        print("Wrong Guess")
        Failed +=1
        if Failed == Max_Num_FalseGuesses:
            print("No More Trials! YOU FAILED!")
            break
        else:
            print("There are " + str(Max_Num_FalseGuesses-Failed)+" Trials")

    print("Currently, your Guess is: ",Guess)

    Check_Complete=True
    for i in range(len(Word)-1):
        if Guess[i] != Word[i]:
            Check_Complete=False
    if Check_Complete:
        print ("Congratulations, YOU WON!")
        break








