"""
File: draw line
Name: Ian
-------------------------
1. import GOval, GLine, GWindow from campy
2. create a window
3. draw circle after the first click of a line
4. draw the line and delete the first circle
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


window = GWindow()
oval = GOval(20, 20)
counter = 1       # the counter of the click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global counter
    if counter == 2:      # the even click
        line = GLine(oval.x+10, oval.y+10, mouse.x, mouse.y)
        window.add(line)        # draw the line from the odd click to the even click
        window.remove(oval)     # remove the oval from the window
        counter = 1
    else:       # the odd click
        oval.x = mouse.x - 10
        oval.y = mouse.y - 10
        window.add(oval)        # move and draw the oval on the odd click
        counter = 2


if __name__ == "__main__":
    main()
