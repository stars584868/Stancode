"""
File: mirror
Name: Ian
----------------------
1. import campy
2. create window
3. draw
"""


from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GLabel, GLine, GArc, GPolygon, GRect


def main():
    """
    TODO:
    """
    window = GWindow(width=800, height=400)
    face = GOval(200, 150, x=300, y=50)
    window.add(face)
    nose = GOval(50, 30, x=370, y=120)
    window.add(nose)
    lt_eye = GOval(10, 10, x=350, y=100)
    lt_eye.filled = True
    lt_eye.fill_color = 'black'
    window.add(lt_eye)
    rt_eye = GOval(10, 10, x=432, y=100)
    rt_eye.filled = True
    rt_eye.fill_color = 'black'
    window.add(rt_eye)
    lt_nose = GRect(2, 10, x= 403, y=130)
    window.add(lt_nose)
    rt_nose = GRect(2, 10, x= 385, y=130)
    window.add(rt_nose)
    lt_ear1 = GLine(332, 70, 360, 30)
    window.add(lt_ear1)
    lt_ear2 = GLine(360, 30, 390, 50)
    window.add(lt_ear2)
    rt_ear1 = GLine(410, 50, 440, 30)
    window.add((rt_ear1))
    rt_ear2 = GLine(440, 30, 470, 70)
    window.add(rt_ear2)
    lt_body = GArc(200,300, 140, 40)
    window.add(lt_body, x=350, y=174)
    rt_body = GArc(200,300, 0, 40)
    window.add(rt_body, x=440, y=172)
    computer = GPolygon()
    computer.add_vertex((330,300))
    computer.add_vertex((480,300))
    computer.add_vertex((530,220))
    computer.add_vertex((280,220))
    computer.filled = True
    computer.fill_color = 'darkgray'
    window.add(computer)
    plate = GRect(154, 10, x=328, y=300)
    plate.filled = True
    plate.fill_color = 'darkgrey'
    window.add(plate)
    table = GRect(500, 20, x=150, y=310)
    table.filled = True
    table.fill_color = 'burlywood'
    window.add(table)


if __name__ == '__main__':
    main()
