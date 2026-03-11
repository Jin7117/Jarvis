import pyautogui
import time
import pytesseract
from PIL import Image
import cv2
import numpy as np
import linksEdit
import pygetwindow as gw

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -------------------------
# BASIC CONTROL
# -------------------------
def open_chrome():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chrome', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

def close_chrome():
    pyautogui.hotkey('alt', 'f4')

def close_all_chrome():
    pyautogui.hotkey('ctrl', 'shift', 'q')

def open_incognito():
    open_chrome()
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')  # switch to regular window
    time.sleep(0.5)
    close_chrome()  # Close the regular window

def focus_chrome_window(incognito=False):
    windows = gw.getWindowsWithTitle("Google Chrome")
    for w in windows:
        title = w.title.lower()
        if incognito and "incognito" in title:
            w.activate()
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "t")
            return True
        if not incognito and "incognito" not in title:
            w.activate()
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "t")
            return True
    return False

# -------------------------
# SEARCH / URL
# -------------------------
def search_google(query):
    pyautogui.hotkey('ctrl', 'l')  # focus address bar
    time.sleep(0.5)
    pyautogui.write(query, interval=0.05)
    pyautogui.press('enter')

def open_website(url):
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.write(url)
    pyautogui.press('enter')

def open_saved_link(name):
    """
    Opens a saved link using smart_search logic
    """
    link = linksEdit.search_link(name)
    if link:
        print(f"Opening saved link: {link['name']}")
        smart_search(link['url'], normal=True)
    else:
        print(f"Link '{name}' not found. Performing normal search...")
        smart_search(name, normal=True)

# -------------------------
# TAB CONTROL
# -------------------------
def new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def reopen_closed_tab():
    pyautogui.hotkey('ctrl', 'shift', 't')

def open_tab_number(n):
    pyautogui.hotkey('ctrl', str(n))  # 1-8

# -------------------------
# PAGE NAVIGATION
# -------------------------
def scroll_down(amount=500):
    pyautogui.scroll(-amount)

def scroll_up(amount=500):
    pyautogui.scroll(amount)

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def refresh_page():
    pyautogui.press('f5')

def hard_refresh():
    pyautogui.hotkey('ctrl', 'shift', 'r')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def reset_zoom():
    pyautogui.hotkey('ctrl', '0')

def find_on_page(text):
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pyautogui.write(text)

def open_downloads():
    pyautogui.hotkey('ctrl', 'j')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def bookmark_page():
    pyautogui.hotkey('ctrl', 'd')

# -------------------------
# SMART SEARCH (Normal/Incognito)
# -------------------------
def smart_search(text, normal=False):
    """
    Opens a query or URL in Chrome:
    - normal=True → normal window
    - normal=False → incognito
    Handles saved links automatically.
    """
    found = focus_or_open()
    if not found:
        if normal:
            open_chrome()
        else:
            open_incognito()

    link = linksEdit.search_link(text)
    if link:
        open_website(link['url'])
    else:
        search_google(text)

# -------------------------
# CHROME WINDOW HELPERS
# -------------------------
def find_chrome_window():
    windows = gw.getWindowsWithTitle("Google Chrome")
    for w in windows:
        try:
            if w.visible and not w.isMinimized and w.width > 200 and w.height > 200:
                return w
        except:
            continue
    return None

def switch_to_window(window):
    if window:
        window.activate()
        return True
    return False

def focus_or_open():
    window = find_chrome_window()
    if window:
        choice = input("Chrome window already open. Switch tab or open new? (s/n): ").lower()
        time.sleep(1)
        switch_to_window(window)
        if choice == "n":
            pyautogui.hotkey("ctrl", "t")
        return True
    return False

# -------------------------
# SCREEN READING
# -------------------------
def read_screen():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    screenshot = cv2.threshold(screenshot, 150, 255, cv2.THRESH_BINARY)[1]
    data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    valid_text = []
    for i in range(len(data["text"])):
        word = data["text"][i]
        confidence = int(data["conf"][i])
        if confidence > 70 and word.strip() != "":
            valid_text.append(word)
    print(" ".join(valid_text))