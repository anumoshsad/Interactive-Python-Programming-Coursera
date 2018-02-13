# http://www.codeskulptor.org/#user41_K8IOUmCO6E_0.py

#"Stopwatch: The Game"
import simplegui

# define global variables
time = 0
text = "00:00.0"
win, total = 0, 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute, second = 0, 0
    if t>5999:
        return "9:59.9"
    else:
        minute = t//600
        second = t- 600 * minute
    minute = str(minute)
    if second < 10:
        second = '00.' + str(second)
    elif second < 100:
        second = str(second)
        second = '0' + second[0] + "." + second[1]
    else:    
        second = str(second)
        second = second[:2]+ '.' + second[2]
    return minute + ':' + second
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global time, win, total
    if timer.is_running():
        timer.stop()
        if time % 10 == 0:
            win += 1
            total +=1
        else: 
            total += 1

def reset():
    global time, win, total
    timer.stop()
    time = 0
    win, total = 0, 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global text, time, win, total
    res = str(win) + '/' + str(total)
    text = format(time)
    canvas.draw_text(text, [65,110], 60, "White")
    canvas.draw_text(res, [200,40], 40, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

frame.start()


