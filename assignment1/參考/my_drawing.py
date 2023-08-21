"""
File: my_drawing.py
Name: Sophia
----------------------
This program draws a fat version of MonaLisa.
"""
from campy.graphics.gobjects import GOval, GRect, GArc, GLabel
from campy.graphics.gwindow import GWindow

WIDTH = 650
HEIGHT = 700


def main():
    """
    Title: Be Happy and Confident

    This is a fat version of MonaLisa; however, she still keeps
    her confidence and wears a smile. I hope to stay optimistic
    just like her no matter what difficulties that I encounter.
    """
    window = GWindow(width=WIDTH, height=HEIGHT, title='my_drawing.py')

    hat1 = GOval(440, 550, x=120, y=25)
    hat1.filled = True
    hat2 = GOval(70, 400, x=490, y=165)
    hat2.filled = True
    hat_line = GArc(410, 400, 20, 130)
    clothes = GOval(680, 680, x=-30, y=410)
    clothes.filled = True

    hair1 = GOval(345, 300, x=165, y=50)
    hair1 = hair_deco(hair1)
    hair2 = GOval(55, 350, x=150, y=170)
    hair2 = hair_deco(hair2)
    hair3 = GOval(80, 200, x=160, y=260)
    hair3 = hair_deco(hair3)
    hair4 = GOval(40, 40, x=410, y=85)
    hair4 = hair_deco(hair4)
    hair5 = GOval(50, 50, x=420, y=110)
    hair5 = hair_deco(hair5)
    hair6 = GOval(50, 50, x=430, y=140)
    hair6 = hair_deco(hair6)
    hair7 = GOval(45, 45, x=440, y=170)
    hair7 = hair_deco(hair7)
    hair8 = GOval(45, 45, x=450, y=200)
    hair8 = hair_deco(hair8)
    hair9 = GOval(45, 45, x=450, y=230)
    hair9 = hair_deco(hair9)
    hair10 = GOval(45, 45, x=450, y=260)
    hair10 = hair_deco(hair10)
    hair11 = GOval(50, 50, x=450, y=300)
    hair11 = hair_deco(hair11)
    hair12 = GOval(50, 50, x=440, y=340)
    hair12 = hair_deco(hair12)
    hair13 = GOval(50, 50, x=440, y=380)
    hair13 = hair_deco(hair13)
    hair14 = GOval(50, 50, x=440, y=420)
    hair14 = hair_deco(hair14)
    hair15 = GOval(40, 40, x=450, y=460)
    hair15 = hair_deco(hair15)
    hair16 = GOval(60, 410, x=460, y=140)
    hair16 = hair_deco(hair16)

    face1 = GOval(310, 260, x=180, y=80)
    face1 = skin_deco(face1)
    face2 = GOval(330, 310, x=170, y=120)
    face2 = skin_deco(face2)

    nose1 = GArc(80, 80, 320, 110)
    nose2 = GArc(80, 80, 122, 110)
    nose3 = GOval(10, 5, x=278, y=267)
    nose3.filled = True
    nose4 = GOval(10, 5, x=298, y=267)
    nose4.filled = True
    nose5 = GArc(15, 15, 100, 100)
    nose6 = GArc(15, 15, 0, 100)

    mouth1 = GArc(70, 70, 220, 95)
    mouth2 = GArc(40, 40, 190, 170)
    mouth2.color = 'salmon'
    mouth3 = GArc(20, 20, 10, 170)
    mouth_deco(mouth3)
    mouth4 = GArc(20, 20, 10, 170)
    mouth_deco(mouth4)
    mouth5 = GOval(38, 12, x=277, y=308)
    mouth_deco(mouth5)

    r_eye = GOval(50, 25, x=200, y=210)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    r_eye_black = GOval(23, 23, x=220, y=211)
    r_eye_black.filled = True
    l_eye = GOval(50, 25, x=340, y=210)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    l_eye_black = GOval(23, 23, x=360, y=211)
    l_eye_black.filled = True

    r_eyebrow = GArc(90, 100, 30, 120)
    l_eyebrow = GArc(90, 100, 30, 120)

    r_eyelash = GArc(70, 70, 40, 130)
    l_eyelash = GArc(70, 70, 40, 130)

    neck = GRect(220, 130, x=240, y=350)
    neck = skin_deco(neck)

    breast1 = GArc(1160, 900, 230, 73)
    breast1 = skin_deco(breast1)
    breast2 = GArc(100, 100, 320, 120)
    breast3 = GArc(100, 100, 100, 160)

    label = GLabel('Always wear a smile : )', x=40, y=680)
    label.font = '-60'
    label.color = 'gold'

    window.add(hat1)
    window.add(clothes)
    window.add(hair1)
    window.add(neck)
    window.add(breast1, x=-10, y=130)
    window.add(hat2)
    window.add(hair2)
    window.add(hair3)
    window.add(face1)
    window.add(face2)
    window.add(hair4)
    window.add(hair5)
    window.add(hair6)
    window.add(hair7)
    window.add(hair8)
    window.add(hair9)
    window.add(hair10)
    window.add(hair11)
    window.add(hair12)
    window.add(hair13)
    window.add(hair14)
    window.add(hair15)
    window.add(r_eye)
    window.add(r_eye_black)
    window.add(l_eye)
    window.add(l_eye_black)
    window.add(hat_line, x=150, y=110)
    window.add(hair16)
    window.add(nose1, x=260, y=205)
    window.add(nose2, x=300, y=200)
    window.add(nose3)
    window.add(nose4)
    window.add(nose5, x=272, y=260)
    window.add(nose6, x=305, y=260)
    window.add(r_eyebrow, x=190, y=180)
    window.add(l_eyebrow, x=330, y=180)
    window.add(mouth2, x=276, y=300)
    window.add(mouth3, x=275, y=305)
    window.add(mouth4, x=295, y=305)
    window.add(mouth5)
    window.add(mouth1, x=270, y=300)
    window.add(breast2, x=260, y=525)
    window.add(breast3, x=300, y=525)
    window.add(r_eyelash, x=195, y=205)
    window.add(l_eyelash, x=335, y=205)
    window.add(label)


def hair_deco(obj):
    """
    This function decorate the hair part in the picture.
    """
    hair_color = 'sienna'
    obj.filled = True
    obj.color = hair_color
    obj.fill_color = hair_color
    return obj


def skin_deco(obj):
    """
    This function decorate the skin part in the picture.
    """
    skin_color = 'papayawhip'
    obj.filled = True
    obj.color = skin_color
    obj.fill_color = skin_color
    return obj


def mouth_deco(obj):
    """
    This function decorate the mouth part in the picture.
    """
    mouth_color = 'salmon'
    obj.filled = True
    obj.color = mouth_color
    obj.fill_color = mouth_color
    return obj


if __name__ == '__main__':
    main()
