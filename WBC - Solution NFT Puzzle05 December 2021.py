#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 05. If you change the LSB of
the image, technically the quality of the image is altered, but since the alter
is so so extremely limited, it's hard (if it's even seen) to see any difference
before and after the alteration.  So for every byte in an image you can "hide" a
single bit. With enough bytes, you can hide whatever fits.
"""

from PIL import Image, ImageMath

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"

def main():
  img = Image.open("1050.png")

  s = img.split()
  expr = 'convert((s & 2**bits - 1) << (8 - bits), "L")'
  out = [ImageMath.eval(expr, s = s[k], bits = 2) for k in range(len(s))] 
  out = Image.merge('RGBA', out)
  out.save("flag.png")
  out.show()

if __name__ == '__main__' :
  main()