import pyautogui
import time
import pygetwindow as gw

def open_spotify():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('spotify', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)


def spotify_search(query):
    open_spotify()
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(query, interval=0.05)
    pyautogui.press('enter')

def playpause():
    pyautogui.press('spacebar')
