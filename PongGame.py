# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = 150
paddle2_pos = 150

paddle1_vel = 0
paddle2_vel = 0

score1 = 0 
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0,0]
    if direction == RIGHT:
        ball_vel = [-random.randrange(2,6),-random.randrange(1,4)]
    else:
        ball_vel = [random.randrange(2,6),-random.randrange(1,4)]
        
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball and determine whether paddle and ball collide    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]/10
        else:
            spawn_ball(LEFT)
            score2 += 1
    if ball_pos[0] >= WIDTH - PAD_WIDTH  - BALL_RADIUS - 1:
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]/10
        else:   
            spawn_ball(RIGHT)
            score1 += 1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] = - ball_vel[1]

            
    # draw ball
    canvas.draw_circle((ball_pos[0],ball_pos[1]), BALL_RADIUS, 3, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos < 0:
        paddle1_pos -= paddle1_vel
    if paddle1_pos > HEIGHT - PAD_HEIGHT + 1:
        paddle1_pos -= paddle1_vel
    if paddle2_pos < 0:
        paddle2_pos -= paddle2_vel
    if paddle2_pos > HEIGHT - PAD_HEIGHT + 1:
        paddle2_pos -= paddle2_vel
        
    # draw paddles
    paddle1 = canvas.draw_line((0,0 + paddle1_pos),(0,PAD_HEIGHT + paddle1_pos), 14, 'White')
    paddle2 = canvas.draw_line((WIDTH,PAD_HEIGHT + paddle2_pos),(WIDTH,0 + paddle2_pos), 14, "White")
     
    # draw scores
    canvas.draw_text(str(score1),(WIDTH/4,100),40,"Blue")
    canvas.draw_text(str(score2),(WIDTH*3/4,100),40,"Blue")    
def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 3
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 3
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("new game" ,new_game)

# start frame
new_game()
frame.start()

