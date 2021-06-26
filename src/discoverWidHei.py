#!/usr/bin/env python3

from PIL import Image

# get the image path
image = ""
img = Image.open(image)

width = img.Width
height = img.Height

print('the height: ',height)
print('the width: ',width)
