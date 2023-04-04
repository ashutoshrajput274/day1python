import random
#Stone=1
#Paper=2
#Sci.=3
#Computer choose a random number in the range of 1 to 3
com = random.randint(1,3)
#Take a input from user
user = int(input('''(Stone:1, Paper:2, Sci.:3) Choose a number :'''))
#Printing that user choose
if user == 1:
    print("\n user choose stone")
elif user == 2:
    print("\n user choose Paper")
elif user == 3:
    print("\n user choose Sci.")
# printing what computer choose
if com == 1:
    print("\n com choose Stone\n")
elif com == 2:
    print("\n com choose Paper\n")
elif com == 3:
    print("\n com choose Sci.\n")
# Game Algo
if com == 1:
    if user == 1:
        print("Game is draw")
    elif user == 2:
        print("user Wins the Game")
    elif user == 3:
        print("com Wins the Game")
elif com == 2:
    if user == 1:
        print("Computer Wins the Game")
    elif user == 2:
        print("Game is draw")
    elif user == 3:
        print("user Wins the Game")
elif com == 3:
    if user == 1:
        print("user Wins the Game")
    elif user == 2:
        print("Com Wins the Game")
    elif user ==3:
        print("Game is draw")

    


    
