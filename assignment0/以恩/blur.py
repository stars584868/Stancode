"""
File: blur.py
Name: Ian
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original picture
    :return: new_img: SimpleImage, blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)
            total_red = 0
            total_blue = 0
            total_green = 0
            total_num = 0
            # first row
            if x == 0:
                lower = x
            else:
                lower = x - 1
            # first column
            if y == 0:
                left = y
            else:
                left = y - 1
            # last row
            if x == (img.width-1):
                higher = x
            else:
                higher = x + 1
            # last column
            if y == (img.height-1):
                right = y
            else:
                right = y + 1

            # add up RGB
            for i in range(left, right+1):
                for j in range(lower, higher+1):
                    total_red += img.get_pixel(i, j).red
                    total_blue += img.get_pixel(i, j).blue
                    total_green += img.get_pixel(i, j).green
                    total_num += 1

            # RGB average
            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blue / total_num

    return new_img


def main():

    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
