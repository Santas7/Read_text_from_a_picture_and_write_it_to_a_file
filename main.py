import pytesseract
from PIL import Image, ImageOps
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def start():
    link = input("Please input link: ")
    photo_files = Image.open(link)
    text_picture = pytesseract.image_to_string(photo_files, config = r"--oem 3 --psm 6")
    file = open('text.doc', 'w')
    file.write(text_picture)
    file.close()

if __name__ == '__main__':
    start() # starting
