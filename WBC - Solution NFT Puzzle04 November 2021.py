#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 04. On the top of every image we added the flag, in text, using a lightly different color than the purple cloud. So if you use photoshop or Photopea (online version of Photoshop) and use the "magic wand" you can see that the text which is slightly off not being selected. Removing the color of the clouds reveals the flag.
"""

import numpy as np
from PIL import Image

im = Image.open('images/768.png')
im = im.convert('RGBA')
data = np.array(im)

r1, g1, b1 = 22, 0, 56
rw, gw, bw, aw = 255, 255, 255, 255
rb, gb, bb, ab = 0, 0, 0, 255

red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

mask = ((red == r1) & (green == g1) & (blue == b1))
data[:,:,:4][mask] = [rw, gw, bw, aw]

im = Image.fromarray(data)

im.save('flag_exposed.png')
im.show()
