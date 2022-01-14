#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is created for Whiteboard crypto to solve the monthly NFT puzzle.
This script outputs the flag needed to solve Puzzle 08. All images in this puzzle
contains the flag at the end of the file. There are many . added to the text to
make it hard to read.
"""

def main():
  with open('images/1792.png','rb') as f:
    buff = f.read()

  flag = buff[729990:730141]
  str = flag.decode()
  print(str.replace('.', ''))

if __name__ == '__main__' :
  main()
