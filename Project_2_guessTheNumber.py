# http://www.codeskulptor.org/#user41_KZ7G7m6I4u_7.py

import random, simplegui

#initial value for range and remaining guesses
Range = 100
remaining = 7

def new_game():   
    global secret_number, Range, remaining
    if Range == 100:
        secret_number, remaining = random.randrange(0,100), 7
    elif Range == 1000:
        secret_number, remaining = random.randrange(0,1000), 10
        
    print "New game. Range is [0,"+str(Range)+")"
    print "Number of remaining guesses is",remaining,"\n"
    
# define event handlers for control panel
def range100():
    global Range
    Range = 100
    new_game()

def range1000():
    global Range
    Range = 1000
    new_game()
    
def input_guess(guess):
    global range, remaining
    guess = int(guess)
    print "Guess was",guess
    remaining -= 1
    print "Number of remaining guesses is",remaining
    if remaining >0:
        if guess > secret_number :
            print "Your Guess is Higher than the Secret Number!\n"
        elif guess < secret_number : 
            print "Your Guess is Lower than the Secret Number!\n"
        else: 
            print "Your Guess is Correct!\n"
            Range, remaining = 100, 7
            new_game()
    elif remaining == 0:
        if guess != secret_number: 
            print "You ran out of guesses. The number was",secret_number,"\n"
            new_game()
        elif guess == secret_number:
            print "Correct!\n"
            new_game()
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
f.start()

