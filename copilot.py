import pyautogui
import time


def open_vscode():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Visual studio', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

def open_copilot():
    open_vscode()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    time.sleep(1)

def open_terminal():
    open_vscode()
    time.sleep(2)
    pyautogui.hotkey('ctrl', '`')