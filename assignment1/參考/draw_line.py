"""
File: draw_line.py
Name: Sophia
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line
appears at the condition where the circle disappears as the
user clicks on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10      # This constant controls the size of the circle.

# Global variable
window = GWindow()
start_x = 0    # The x of starting point of the line.
start_y = 0    # The y of starting point of the line.
circle = None  # The hollow circle indicating the first click.
count = 0      # Counting the times of the user's click.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line
    appears at the condition where the circle disappears as the
    user clicks on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):
    """
    This function draws a hollow circle centered the mouse at odd
    click, and it draws a line starting with the odd click mouse
    and ending with the next click mouse at even click.
    """
    global count, start_x, start_y, circle
    count += 1
    if count % 2 == 1:
        circle = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        window.add(circle)
        start_x = circle.x
        start_y = circle.y
    else:
        window.remove(circle)
        line = GLine(start_x + SIZE / 2, start_y + SIZE / 2, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
