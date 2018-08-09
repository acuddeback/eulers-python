#imports random function
import random
#introduces the game to the user
print('''
How to play:
When Prompted, enter one of the following:
    Rock
    Paper
    Scissors
''')
#sets up boolean to keep game running
gameLoop = True
#lists acceptable user inputs
acceptable_input = ["Rock","rock","Paper","paper","Scissors","scissors"]
#lists possible computer moves
computer_move_list = ["rock", "paper", "scissors"]
#keeps program running until user says they are done
while gameLoop == True:
    #sets value for computer generated move
    computer_move = random.choice(computer_move_list)
    #takes input from user
    user_move = raw_input("Make your move! Enter 'r8ck' paper' or 'scissors' ")
    #checks to see if user input is acceptable
    if user_move not in acceptable_input:
        #sets boolean so the program can keep prompting the user as long as the input is unacceptable
        acceptableInput = False
        while acceptableInput == False:
            #prompts user to re-enter their move
            user_move = raw_input("Uh oh, I don't recognize that move! Enter 'rock' paper' or 'scissors' ")
            #sets boolean to exit the loop if the input is acceptable
            if user_move in acceptable_input:
                acceptableInput = True
    #chain of events if user inputs rock
    if user_move in ("rock", "Rock"):
        #outcome when computer plays rock
        if computer_move == "rock":
            print("Your opponent played Rock... it's a tie!")
        #outcome when computer plays paper
        elif computer_move == "paper":
            print("Your opponent played Paper... you lose!")
        #outcome when computer plays scissors
        elif computer_move == "scissors":
            print("Your opponent played Scissors... you win!")
    #chain of events if user inputs paper
    elif user_move in ("paper", "Paper"):
        #outcome when computer plays rock
        if computer_move == "rock":
            print("Your opponent played Rock... you win!")
        #outcome when computer plays paper
        elif computer_move == "paper":
            print("Your opponent played Paper... it's a tie!")
        #outcome when computer plays scissors
        elif computer_move == "scissors":
            print("Your opponent played Scissors... you lose!")
    #chain of events if user inputs scissors
    elif user_move in ("scissors", "Scissors"):
        #outcome when computer plays rock
        if computer_move == "rock":
            print("Your opponent played Rock... you lose!")
        #outcome when computer plays paper
        elif computer_move == "paper":
            print("Your opponent played Paper... you win!")
        #outcome when computer plays scissors
        elif computer_move == "scissors":
            print("Your opponent played Scissors... it's a tie!")
    play_again = raw_input("Would you like to play again? Enter 'yes' or 'no' ")
    #checks to see if user input is acceptable
    if play_again not in ("yes", "Yes", "no", "No"):
        #sets boolean so the program can keep prompting the user as long as the input is unacceptable
        acceptableInput = False
        while acceptableInput == False:
            #prompts user to re-enter their move
            play_again = raw_input("I'm not sure what you mean. Enter 'yes' or 'no' ")
            #sets boolean to exit the loop if the input is acceptable
            if play_again in ("yes", "Yes", "no", "No"):
                acceptableInput = True
    #terminates the program if the user no longer wants to play
    if play_again in ("No", "no"):
        gameLoop = False
