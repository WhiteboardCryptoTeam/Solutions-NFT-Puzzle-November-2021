#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 06. Where Puzzle 05 is hiding an image, Puzzle 06 is hiding text. The text that is hidden is also ROT13 (a simple letter substitution cipher by rotating the letters 13 places in the alphabet). After using the cipher rotation revelas the flag.
"""


from PIL import Image
import codecs

def decode(img):
  image = Image.open(img, 'r')
  data = ''
  imgdata = iter(image.getdata())

  while (True):
    pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
    binstr = ''

    for i in pixels[:8]:
      if (i % 2 == 0):
        binstr += '0'
      else:
        binstr += '1'

    data += chr(int(binstr, 2))
    if (pixels[-1] % 2 != 0):
      return data

def main():
  image = "images/1363.png"
  print("Flag:         " + codecs.decode(decode(image), 'rot_13'))
  print("Flag (ROT13): " + decode(image))

if __name__ == '__main__' :
  main()