import pyautogui
import time
import pytesseract
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_screen():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    screenshot = cv2.threshold(screenshot,150,255,cv2.THRESH_BINARY)[1]
    data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    valid_text = []
    for i in range(len(data["text"])):
        word = data["text"][i]
        confidence = int(data["conf"][i])
        if confidence >70  and word.strip() != "":
            valid_text.append(word)
    print(" ".join(valid_text))

time.sleep(2)  # Give user time to switch to the desired screen
read_screen()