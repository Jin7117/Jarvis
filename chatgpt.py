import pyautogui
import time
import pygetwindow as gw

def open_chatgpt():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chatgpt', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)


def search_chatgpt(query):
    open_chatgpt()
    pyautogui.write(query, interval=0.05)
    pyautogui.press('enter')

def victoria():
    open_chatgpt()
    pyautogui.hotkey('ctrl' , 'alt' , 'v')
    time.sleep(2)
