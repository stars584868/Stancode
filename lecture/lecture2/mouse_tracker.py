"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 100
rect = GRect(SIZE, SIZE)
window = GWindow()


def main():
	rect.filled = True
	window.add(rect)
	onmousemoved(position)
	onmousedragged(draw)
	onmouseclicked(draw)


def position(event):
	rect.x = event.x - rect.width/2
	rect.y = event.y - rect.height/2


def draw(mouse):
	hole = GRect(SIZE, SIZE)
	hole.filled = True
	window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
	main()
