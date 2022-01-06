from PIL import Image
from pathlib import Path

# img  = Image.open(path)
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)

path = Path("/Users/ebolee/repo/code_challenge/py-mini-apps")
filename = "image.jpg"

try:
    img = Image.open(filename)
except IOError:
    print(IOError.errno)
# Use the above statement within try block, as it can
# raise an IOError if file cannot be found,
# or image cannot be opened.


def rotate():
    try:
        # Relative Path
        img = Image.open("image.jpg")

        # Angle given
        img = img.rotate(180)

        # Saved in the same relative location
        img.save("rotated_picture.jpg")

    except IOError:
        print(IOError)


def crop():
    try:
        # Relative Path
        img = Image.open("image.jpg")
        width, height = img.size

        area = (0, 0, width / 2, height / 2)
        img = img.crop(area)

        # Saved in the same relative location
        img.save("cropped_picture.jpg")

    except IOError:
        print(IOError)


def resize():
    try:
        # Relative Path
        img = Image.open("image.jpg")
        width, height = img.size

        img = img.resize((int(width / 2), int(height / 2)))

        # Saved in the same relative location
        img.save("resized_picture.jpg")
    except IOError:
        print(IOError)


def paste():
    try:
        # Relative Path
        # Image on which we want to paste
        img = Image.open("image.jpg")

        # Relative Path
        # Image which we want to paste
        img2 = Image.open("image2.jpeg")
        img.paste(img2, (50, 50))

        # Saved in the same relative location
        img.save("pasted_picture.jpg")

    except IOError:
        print(IOError)


def histogram():
    try:
        # Relative Path
        img = Image.open("image.jpg")

        # Getting histogram of image
        print(img.histogram())

    except IOError:
        print(IOError)


def transposed():
    try:
        # Relative Path
        img = Image.open("image.jpg")

        # transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save transposed image
        transposed_img.save("transposed.jpg")
    except IOError:
        print(IOError)


def to_rgb():
    try:
        # Relative Path
        img = Image.open("image.jpg")

        # splitting the image
        print(img.split())
    except IOError:
        print(IOError)


def tobitmap():
    try:
        # Relative Path
        img = Image.open("image.jpg")
        print(img.mode)
        # converting image to bitmap
        print(img.tobitmap())
        print(type(img.tobitmap()))
    except IOError:
        print(IOError)


def to_thumbnail():
    try:
        # Relative Path
        img = Image.open("image.jpg")

        # In-place modification
        img.thumbnail((200, 200))

        img.save("thumb.jpg")
    except IOError:
        print(IOError)


if __name__ == "__main__":
    rotate()
    crop()
    resize()
    paste()
    histogram()
    transposed()
    to_rgb()
    tobitmap()
    to_thumbnail()

