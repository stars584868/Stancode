"""
File: blur.py
Name: Sophia
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""
from simpleimage import SimpleImage


def blur(img):
    """
    Function: This function blurs the original image.
    :param img: old_img, the original smiling face image.
    :return new_img: SimpleImage, the blurred image that we processed.
    """
    # Creating a new blank img that is as big as the original one.
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the image.
    for x in range(img.width):
        for y in range(img.height):
            new_p = new_img.get_pixel(x, y)  # Getting pixel of new_img at x,y.
            r_sum = 0  # The sum of red pixels of (x, y) and all its neighbors.
            g_sum = 0  # The sum of green pixels of (x, y) and all its neighbors.
            b_sum = 0  # The sum of blue pixels of (x, y) and all its neighbors.
            count = 0  # Counting the number of neighbor at (x, y).
            # Loop over the neighbors and itself.
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + i
                    # Checking whether the pixel is within the range of image.
                    if 0 <= pixel_x < img.width:           # True. Within the image.
                        if 0 <= pixel_y < img.height:      # True. Within the image.
                            # Getting pixel of original image at (pixel_x, pixel_y).
                            old_p = img.get_pixel(pixel_x, pixel_y)
                            r_sum += old_p.red    # Computing the sum of red pixels.
                            g_sum += old_p.green  # Computing the sum of green pixels.
                            b_sum += old_p.blue   # Computing the sum of blue pixels.
                            count += 1    # The number of neighbors increases by one.
            # Blurring image by computing average pixels of itself and its neighbors.
            new_p.red = r_sum / count
            new_p.green = g_sum / count
            new_p.blue = b_sum / count
    return new_img  # Returning the blurred image that we processed.


def main():
    """
    This function shows original and blurred smiling face image that we processed.
    """
    # Importing and showing the original image.
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    # Showing the processed image.
    blurred_img = blur(old_img)
    for i in range(5):  # Setting blurring the image for how many times.
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
