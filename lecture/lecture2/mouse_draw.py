"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged, onmouseclicked

# This constant controls the size of the hole
SIZE = 30
window = GWindow()


def main():
	onmousedragged(draw)
	onmouseclicked(draw)


def draw(mouse):
	hole = GOval(SIZE, SIZE)
	hole.filled = True
	window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
	main()
