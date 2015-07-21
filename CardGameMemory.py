# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global DECK, EXPOSED
    EXPOSED = [False, False, False, False, False, False, False, False,
               False, False, False,
               False,False , False, False, False] 
    DECK = ([1,2,3,4,5,6,7,8]+
            [1,2,3,4,5,6,7,8])
    random.shuffle(DECK)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global EXPOSED
    card_cliked = int(pos[0]/50)
    if not EXPOSED[card_cliked]:
        EXPOSED[card_cliked] = True
    print card_cliked
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARDS, EXPOSED
    for i in range(len(DECK)):
        if EXPOSED[i]:
            canvas.draw_text(str(DECK[i]),((50*i)+17,60),20,'White')
        else:
            canvas.draw_polygon([[0+(i*50), 0], [50+(i*50), 0], [50+(i*50), 100], 
                                 [0+(i*50), 100]], 1, 'Yellow', 'Green' )

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric