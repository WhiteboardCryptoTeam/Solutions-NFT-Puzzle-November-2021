#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 01. The NFT contains
a red or blue pixel in the top left corner which represents a 0 or 1.
When the binary string is converted to ASCII it contains the flag.
"""

from PIL import Image

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"


def decode():
  flag = ""

  for x in range(0,256):
    image = Image.open("images/{}.png".format(x), "r")
    image_rgb = image.convert("RGB")
    r, g, b = image_rgb.getpixel((1, 1))
    if(r == 128 and g == 0 and b == 0):
      flag += "1"
    elif(r == 0 and g == 0 and b == 128):
      flag += "0"

  binary_int = int(flag, 2)
  byte_number = binary_int.bit_length() + 7 // 8
  binary_array = binary_int.to_bytes(byte_number, "big")
  ascii_text = binary_array.decode()

  flag = ascii_text
  return flag

def main():
  print("Flag: " + decode())

if __name__ == '__main__' :
  main()
