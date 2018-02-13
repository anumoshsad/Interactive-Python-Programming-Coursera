# http://www.codeskulptor.org/#user42_ZmJ4LHyjgQ_1.py

# implementation of card game - Memory

import simplegui
import random

turn = 0
# helper function to initialize globals
def new_game():
    global state, cards, exposed, prev
    prev = [-1,-1]
    turn = 0
    state = 0
    cards = list(range(8)) + list(range(8))
    random.shuffle(cards)
    exposed = [False]*16
      

     
# define event handlers
def mouseclick(pos):
    global state,turn
    # add game state logic here
    
    idx = pos[0]/50
    if not exposed[idx]:
        exposed[idx]=True
        if state == 0:
            state = 1
            turn+=1
            
        elif state == 1:
            state = 2
        else:
            if cards[prev[0]]!=cards[prev[1]]:
                exposed[prev[0]]=False
                exposed[prev[1]]=False
                
            state = 1
            turn+=1
        
        prev[state-1] = idx
        label.set_text("Turns = "+str(turn))
 
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = [50 * card_index+10, 70]
        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]), card_pos, 70, 'White')
        else:
            canvas.draw_polygon([(50 * card_index,0),(50 * card_index+50,0),(50 * card_index+50,100),(50 * card_index,100)],2,'black', 'green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric