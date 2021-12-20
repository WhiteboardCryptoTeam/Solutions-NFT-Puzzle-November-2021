# Solutions-NFT-Puzzle-December-2021
This repository contains all scripts to solve the December 2021 NFT puzzle for whiteboardcrypto.com.

# Puzzle 01

So the first puzzle was the simplest in our opinion, but was the last one to be solved. In the top left corner of the image itself, we added a single pixel to every image for this puzzle which was either red or blue representing either a 0 or 1. Since we said that all flags are in the format WBC{TEXT}, you should know the binary form should be converted to text. So a simple google search with "binary to text" should have been enough. Technically it's binary to ASCII :wink:

:checkered_flag: WBC{I_L0VE_P1X3L_4RT_S0_MUCH!1!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle01%20December%202021.py) to the script. 

# Puzzle 02

This puzzle was about the metadata of an image. Every image can contain metadata like the author, comment, description etc. One of the fields in the metadata is "comment". We added the words "one" and "zero" to every image for this puzzle to create a binary string which needed to be converted to ASCII which contained the flag.

:checkered_flag: WBC{WHO_C4R3S_4B0UT_M3T4D4T4!?!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle02%20December%202021.py) to the script.

# Puzzle 03

In our opinion this was the hardest puzzle to be solved even though it was solved quite quickly. We added an encrypted ZIP file, in binary form, to image 666.png. The data is appended to the image (bytes in the end of the file) so the image is not corrupted. If you open the image in a hex editor you can see data appended to the image since a PNG file ends with "END" normally. You can extract the bytes and save it to a file to have a ZIP file. The ZIP file is password protected though. The password for the zip file was "hidden" in image 700.png. The password can be found in plain-text by opening image 700.png in a text editor and scroll all the way down. All the other images we appended some bogus data to make it a little bit harder.

:checkered_flag: WBC{1M_S0RRY_F0R_TH3_ENCRYPT10N}

# Puzzle 04

On the top of every image we added the flag, in text, using a lightly different color than the purple cloud. So if you use photoshop or Photopea (online version of Photoshop) and use the "magic wand" you can see that the text which is slightly off not being selected. Removing the color of the clouds reveals the flag.

:checkered_flag: WBC{N0_W4Y_TH3R3_4R3_2_1M4G3ZZ!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle04%20December%202021.py) to the script.

# Puzzle 05

This puzzle uses the "Least Significant Bit" to hide data. The LSB is the last bit in a byte 00000001 <- the 1 in this binary string. If you change the LSB of the image, technically the quality of the image is altered, but since the alter is so so extremely limited, it's hard (if it's even seen) to see any difference before and after the alteration. So for every byte in an image you can "hide" a single bit. With enough bytes, you can hide whatever fits. Taking every last bit in a byte reveals another image which contains the flag.

:checkered_flag: WBC{ST3GAN0GR4PHY_1S_TH3_B3ST!!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle05%20December%202021.py) to the script.

# Puzzle 06

Where Puzzle 05 is hiding an image, Puzzle 06 is hiding text. The text that is hidden is also ROT13 (a simple letter substitution cipher by rotating the letters 13 places in the alphabet). After using the cipher rotation revelas the flag.

:checkered_flag: WBC{SUBST1TUT10N_C1PH3R_R0T13!!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle06%20December%202021.py) to the script.

# Puzzle 07

The flag for Puzzle 07 is hidden at the end of every file but now stored with the letter substitution cipher ROT47. The cipher ROT13 is well known, but ROT47 is not. The flag uses ROT47 so it's hard to find. If you take the flag and you apply ROT47, it reveals the flag.

:checkered_flag: WBC{R0T47_1S_B3TT3R_TH4N_ROT13!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle07%20December%202021.py) to the script.

# Puzzle 08

In the last puzzle the flag is hidden at the end of every data by appending the data. We made it a bit more difficult by adding a lot of ... between the characters so it was harder to read the flag. Removing the dots reveals the flag.

:checkered_flag: WBC{TH1S_1S_H4RD_T0_R34D!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle08%20December%202021.py) to the script.
