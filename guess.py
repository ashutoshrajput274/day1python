#guess the number
#actual number = 45
#guess = 5
#computer: your guess was too slow
'''Question. store any number in a variable. You have to guess
that number . Your program should be able to tell weather the 
number you guessed was lesser or greater than the actual 
number. you have to finally tell the number of attempts it took
the gressure to guess the number.'''
actual_number = 45
attempts = 0

while True:
    attempts+=1
    guess = int(input("guess the number:\n"))
    if guess<actual_number:
        print("your guess was too low")
    elif guess>actual_number:
        print("your guess too high")
    else:
        print(f"you guess the number is {attempts}attempts")
        break
    print("thanks for playing!")