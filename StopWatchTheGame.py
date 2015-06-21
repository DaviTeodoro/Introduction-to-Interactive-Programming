# template for "Stopwatch: The Game"

# define global variables
import simplegui

time = 0
player_points = 0
comp_points = 0
stoped = True 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t/600
    BC = t/10 - (int(A) * 60)
    D = t - (int(A) * 600) - (BC * 10)
    
    return str(A)+":"+ str(BC) + "." + str(D) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stoped
    stoped = False
    t.start()
    

def stop():
    global player_points
    global comp_points
    global time
    global stoped
    
    if time % 10 == 0 and not stoped:
        player_points += 1
    elif time % 10 != 0 and not stoped:
        comp_points += 1
    
    t.stop()
    stoped = True
    
    

def reset():
    global time 
    global player_points
    global comp_points
    time = 0
    player_points = 0
    comp_points = 0
    t.stop()
    
    

# define event handler for timer with 0.1 sec interval
def timer_tick():
    global time
    time += 1

# define draw handler
def draw_timer(canvas):
    global time
    global comp_points
    global player_points
    canvas.draw_text(format(time), (140, 110), 30, "White")
    canvas.draw_text(str(comp_points)+"/"+str(player_points),(190, 20), 20, "Red")

    
# create frame
f = simplegui.create_frame("Stopwatch: The game", 300, 200)
t = simplegui.create_timer(100, timer_tick)

# register event handlers
f.add_button("Start", start, 60)
f.add_button("Stop", stop, 60)
f.add_button("Reset", reset, 60)
f.set_draw_handler(draw_timer)



# start frame
f.start()

# Please remember to review the grading rubric
