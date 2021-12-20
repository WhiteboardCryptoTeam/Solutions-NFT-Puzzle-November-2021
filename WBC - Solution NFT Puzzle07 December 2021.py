#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 07.
"""

import codecs

__author__ = "Whiteboard Crypto"
__copyright__ = "Copyright 2021, Whiteboard Crypto"
__credits__ = ["Theodore"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Whiteboard Crypto"
__email__ = "whiteboardcryptoteam@gmail.com"
__status__ = "Development"

def rot47(data):
  decode = []
  for i in range(len(data)):
    encoded = ord(data[i])
    if encoded >= 33 and encoded <= 126:
      decode.append(chr(33 + ((encoded + 14) % 94)))
    else:
      decode.append(data[i])
  return ''.join(decode)

def main():

  with open('images/1536.png','rb') as f:
    buff = f.read().hex()

  flag_rot47 = buff[1439630:1439694]

  bytes_object = bytes.fromhex(flag_rot47)
  ascii_string = bytes_object.decode("ASCII")

  print ("Flag (ROT47): " + ascii_string)
  print ("Flag: " + rot47(ascii_string))

if __name__ == '__main__' :
  main()