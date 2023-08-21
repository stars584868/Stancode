"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Whack a mole')
score = 0
score_label = GLabel('Scores'+str(score))


def main():
    score_label.font = '-80'
    window.add(score_label, x=0, y=score_label.height)
    onmouseclicked(remove)
    while True:
        mole = GImage('mole.png')
        random_x = random.randint(0, window.width-mole.width)
        random_y = random.randint(0, window.height - mole.height)
        window.add(mole, x=random_x, y=random_y)
        pause(DELAY)


def remove(mouse):
    global score
    maybe_mole = window.get_object_at(mouse.x, mouse.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        score += 1
        score_label.text = 'Scores'+str(score)
        window.remove(maybe_mole)


if __name__ == '__main__':
    main()
