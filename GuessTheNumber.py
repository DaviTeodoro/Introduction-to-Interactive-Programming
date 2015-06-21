# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random 
import math

secret_number = 0
range_numb = 100
guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global range_numb
    secret_number = random.randrange(0,range_numb)
    print "New Game! Guess a number between 0 and", range_numb

    
    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_numb 
    global guesses
    guesses = 7
    range_numb = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_numb
    global guesses
    guesses = 10
    range_numb = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global guesses
    guess = int(guess)
    print "Guess was ", guess
    
    if  guess > secret_number and guesses > 0:
        print "Lower"
        guesses -= 1
        print "You have", guesses, "guesses left!"
    elif guess < secret_number and guesses > 0:
        print "Higher"
        guesses -= 1
        print "You have", guesses, "guesses left!"
    elif guess == secret_number:
        print "Correct!"
        print
        new_game()
    else:
        print "You lost the game... =("
        print
        new_game()

    
# create frame
f = simplegui.create_frame('Guess the Number', 300, 300)


# register event handlers for control elements and start frame
f.start()
f.add_button('0-100', range100, 60)
f.add_button('0-1000', range1000, 60)
f.add_input('My Guess', input_guess, 50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
