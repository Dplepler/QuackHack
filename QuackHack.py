from PIL import Image
import pytesseract
import numpy as np
from numpy import asarray
import cv2
import time
import matplotlib.pyplot as plt
import pyglet
import pyautogui
import sys
import re
import msvcrt
from pynput.keyboard import Key, Controller, Listener
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\Tesseract'

def read():

   
    current = set()
    keyboard = Controller()
    
    yes = True
    imageNumber = 1
    
    
    while yes:
        
        if msvcrt.kbhit():
            key_pressed = msvcrt.getch()
            print(key_pressed)
            if key_pressed == b'\x1b':
                sys.exit()
               
            
            
        
        pyautogui.screenshot('Screen/Image' + str(imageNumber) + '.jpg')
        screenshot = Image.open('Screen/Image' + str(imageNumber) + '.jpg')
        croppedImage = screenshot.crop((370, 400, 450, 900))
        croppedImage.save('croppedImage.jpg')
        imgAr = asarray(croppedImage).copy()
        
        
        for eachRow in imgAr:
            for eachPix in eachRow:
                if eachPix[0] > 215 and eachPix[1] > 215 and eachPix[2] > 215:
                    eachPix[0] = 0
                    eachPix[1] = 0
                    eachPix[2] = 0
                else:
                    eachPix[0] = 255
                    eachPix[1] = 255
                    eachPix[2] = 255
        newImage = Image.fromarray(imgAr)
        newImage.save('newImage.jpg')
        
        code = pytesseract.image_to_string(Image.open('newImage.jpg'))
        
        if code == "":
            yes = True
        else:
            
            if re.match("^[A-Za-z0-9]*$", code):
                if len(code) >= 4:
                    code.lower()
                    keyboard.type(".pick " + code)
                    keyboard.press(Key.enter)
                    time.sleep(20)
                    yes = True
                else:
                    yes = True
        
            else:
                yes = True
           

        
def main():
  
    read()
    

if __name__ == "__main__":
    main()