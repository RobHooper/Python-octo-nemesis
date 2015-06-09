#!/usr/bin/python2.7
import PIL
import Image

im = Image.open("paris.jpg")

# Image info
print im.format, im.size, im.mode

# Print image
im.show()
