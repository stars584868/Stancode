"""
File: my_drawing.py
Name: 
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800,height=500, title='MyFace')
    l_eye = GOval(50, 50, x=390, y=230)
    l_eye.filled = True
    l_eye.fill_color = 'blue'
    window.add(l_eye)
    mouth = GRect(120, 40, x=390, y=360)
    window.add(mouth)
    label_new = GLabel('Hi', x= 600, y = 300)
    label_new.font = '-30'
    label_new.text = 'new'
    label_new.color = 'magenta'
    window.add(label_new)
    label_yo = GLabel('Yo')
    label_yo.font = '-60'
    window.add(label_yo, x=0, y=label_yo.height)



if __name__ == '__main__':
    main()
