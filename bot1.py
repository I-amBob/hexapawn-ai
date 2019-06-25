####################################################################
#                                                                  #
#                                                                  #
#                                                                  #
#                   github.com/I-amBob/hexapawn-ai                 #
#                                                                  #
#               HEXAPAWN ARTIFICIAL INTELLIGENCE BOT               #
#                                                                  #
#                       by Ciobanu Stefan                          #
#                                                                  #
#                                                                  #
####################################################################


import random  # For choosing random string

s210 = ['green', 'purple']           # Posibility lists
s220 = ['green', 'blue']
s410 = ['purple', 'blue', 'green']
s420 = ['green', 'purple', 'blue']
s430 = ['purple', 'green']
s440 = ['red']
s450 = ['purple', 'blue']
s460 = ['green', 'purple', 'blue']
s470 = ['green', 'purple']
s480 = ['green', 'purple']
s490 = ['purple', 'blue', 'red', 'green']
s411 = ['blue']
s412 = ['purple', 'red']
s610 = ['purple', 'red']
s620 = ['red', 'purple']
s630 = ['purple', 'blue']
s640 = ['blue']
s650 = ['green', 'red']
s660 = ['green', 'purple']
s670 = ['green', 'purple', 'red']
s680 = ['green', 'blue']
s690 = ['purple', 'red']
s611 = ['red', 'purple']
s612 = ['purple', 'blue']
done = 4

gameRules = "Game Rules: "
print("Welcome to the Chess AI")  # Intro
print("#######################")  # Intro

print("Do you know the rules?(y/n)")
knowGR = input(": ")

if knowGR == "n":
    print(gameRules)

print("Let's Start!")

true = 1   #
truef = 1  # For loops
truea = 1  #


while truef < 10:

    while true < 4:
        currentSituationInput: object = eval(input("Current Situation: "))  # User needs to input the current situation of the players
        if currentSituationInput == done:  # For ending the game before round 6
            true = 4                       # Escaping the loop
        else:
            currentSituation: object = currentSituationInput  # For making the input not be the same as the last situation when game finishes before round 6
            move = random.choice(currentSituation)  # Assigning the random choice to a variable
            print(move)  # Printing the choice
            true+=1  # Progressing the loop

    print("Did I win? (y/n)")  # The program needs to know if the computer won or not
    win = input(": ")
    if win == "y":
        currentSituation.append(move)  # If the choice was right, the chances for it to be made again are bigger
    if win == "n":
        if len(currentSituation) != 1:  # To prevent removing all the choices from a variable
            currentSituation.remove(move)  # To remove the bad choice from the variable
    true = 1  # To restart the loop
