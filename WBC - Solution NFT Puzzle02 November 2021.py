#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 02. The images 256 to 511
contains the words "zero" or "one" in the "message" metadata and creates a binary string.
When the binary string is converted to ASCII it contains the flag.
"""

import exiftool

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"

def PyExifTool(pathname):
  with exiftool.ExifTool() as et:
    metadata = et.get_metadata(pathname)
  dt = metadata['PNG:Comment']

  return dt

def decode():
  flag = ""

  for x in range(256,512):
    str = PyExifTool("images/{}.png".format(x))
    if(str == "one"):
      flag += "1"
    elif(str == "zero"):
      flag+= "0"

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
