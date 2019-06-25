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

true = 1
truef = 1
truea = 1


while truef < 10:

    while true < 4:
        currentSituationInput: object = eval(input("Current Situation: "))  # User needs to input the current situation of the players
        if currentSituationInput == done:
            true = 4
        else:
            currentSituation: object = currentSituationInput
            move = random.choice(currentSituation)
            print(move)
            true+=1

    print("Did I win? (y/n)")
    win = input(": ")
    if win == "y":
        currentSituation.append(move)
    if win == "n":
        if len(currentSituation) != 1:
            currentSituation.remove(move)
    true = 1
