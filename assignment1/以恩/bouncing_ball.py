"""
File: bouncing ball
Name: Ian
-------------------------
1. build a window and draw the ball
2. make the mouse clip start the function drop
3. separate the function drop into two conditions: hit the floor, and in the air
"""

from campy.graphics.gobjects import GOval
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(drop)
    window.add(ball)


def drop(mouse):
    vy = 0      # the variable vertical speed of the ball
    out_of_window = 0       # count the number of the ball exceed the width of the window
    while True:
        ball.x += VX        # the horizontal movement of the ball
        if ball.y + SIZE >= window.height:      # when the ball hit the floor
            vy *= -REDUCE
            ball.y += vy
        if ball.x + SIZE >= window.width:       # when the ball exceed the width of the window
            out_of_window += 1
            if out_of_window == 3:
                ball.x = START_X
                ball.y = START_Y
                break
        else:       # when the ball do not hit the floor
            vy += GRAVITY
            ball.y += vy
        pause(DELAY)


if __name__ == "__main__":
    main()
