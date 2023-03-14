# Free-Geek-Stickers
In order to ensure that devices can continue to be reasonably labeled in the future, we created a Python program that generates a PDF with sequential sticker numbers. This code can be found on GitHub here.

This file contains:
**nextID.txt**: a text file containing the next sequential number that hasn’t been generated

**freeGeekStickerGenerator.py**: the python code that when run from the terminal, prompts the user for a number of pages and then returns a PDF with sequential numbers starting at the one in nextID.txt that is that number of pages long

**GenerationDates.csv**: a csv file containing timestamps for when each number was generated

**StickersIDX-Y**: Any PDFs generated thus far, with X and Y being the range of numbers they contain.

**SinglePageStickers.pdf**: blank template for the sticker sheets

When you run this program, it will first prompt you for the number of pages that you would like to generate. There are 80 stickers per page using the Avery 5267 sticker sheets. 

The program then uses an external text document to look up the next number that hasn’t been used. If multiple people are using this code on different computers, it will be necessary to keep track of this number via pushing to GitHub or manually, otherwise the program will do it for you. 

The program also updates a CSV file with the dates and times of when each number is generated. Since it takes weeks for even a single sheet of stickers to be used, this data is likely not helpful, but it does exist and is another instance of something that will need to be pushed/moved if multiple computers are used to generate stickers. 

The PDF it generates will be labeled with the range of IDs that it contains. 

