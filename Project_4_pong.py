# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user41_h9g12OMSRe_0.py

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


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120,240)/60.,-random.randrange(60,180)/60.]
    else:
        ball_vel = [-random.randrange(120,240)/60.,-random.randrange(60,180)/60.]
    
        


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    paddle1_pos, paddle2_pos = HEIGHT/2, HEIGHT/2
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    spawn_ball(bool(random.randrange(2)))
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), (240, 50), 40, 'Red')
    canvas.draw_text(str(score2), (340, 50), 40, 'Red')
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -1 * ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos + paddle1_vel < HALF_PAD_HEIGHT or paddle1_pos + paddle1_vel >HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos -= paddle1_vel
    if paddle2_pos + paddle2_vel < HALF_PAD_HEIGHT or paddle2_pos + paddle2_vel >HEIGHT - HALF_PAD_HEIGHT:
            paddle2_pos -= paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos-HALF_PAD_HEIGHT), 
                         (PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT), 
                         (PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT),
                        (0, paddle1_pos+HALF_PAD_HEIGHT)], 1, 'White', 'White')
    canvas.draw_polygon([(WIDTH, paddle2_pos-HALF_PAD_HEIGHT), 
                         (WIDTH - PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT), 
                         (WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT),
                        (WIDTH, paddle2_pos+HALF_PAD_HEIGHT)], 1, 'White', 'White')
    
    # determine whether paddle and ball collide
    x, y, r = ball_pos[0], ball_pos[1], BALL_RADIUS
    if x-r <= PAD_WIDTH and y >= paddle1_pos - HALF_PAD_HEIGHT and y <= paddle1_pos + HALF_PAD_HEIGHT:
        ball_vel[0] = -1.1*ball_vel[0]
    elif x+r >= WIDTH - PAD_WIDTH and y >= paddle2_pos - HALF_PAD_HEIGHT and y <= paddle2_pos + HALF_PAD_HEIGHT:
        ball_vel[0] = -1.1*ball_vel[0]
    elif x-r <= PAD_WIDTH:
        score2+=1
        spawn_ball(RIGHT)
    elif x+r >= WIDTH - PAD_WIDTH:
        score1+=1
        spawn_ball(LEFT)
    
    # draw scores
    canvas.draw_text(str(score1), (240, 50), 40, 'Red')
    canvas.draw_text(str(score2), (340, 50), 40, 'Red')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -4
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 4
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 4
   
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
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
