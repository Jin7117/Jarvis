import pyautogui
import time
import linkFunctions
import pygetwindow as gw


# -------------------------
# BASIC CONTROL
# -------------------------
def open_chrome():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chrome', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')


def close_chrome():
    window = find_chrome_window()
    if window:
        switch_to_window()
        pyautogui.hotkey('alt', 'f4')
    else :
        print("No window available")

def close_all_chrome():
    print("You sure you wanna close all windows of chrome?")
    target = input("y or n")
    if target == "y":
        window = find_chrome_window()
        if window:
            switch_to_window()
            pyautogui.hotkey('ctrl', 'shift', 'q')
        else :
            print("No window available")
    else:
        print("Command not executed")
    

def open_incognito():
    open_chrome()
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')  # switch to regular window
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')

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
    link = linkFunctions.py.search_link(name)
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
 
    found = focus_or_open()
    if not found:
        if normal:
            open_chrome()
        else:
            open_incognito()

    link = linkFunctions.search_link(text)
    if link:
        open_website(link['url'])
    else:
        search_google(text)

# -------------------------
# CHROME WINDOW HELPERS
# -------------------------


def find_chrome_window():
    windows = gw.getWindowsWithTitle("Google Chrome")

    # First pass: look for incognito windows
    for w in windows:
        try:
            if w.visible and not w.isMinimized and w.width > 200 and w.height > 200:
                if "Incognito" in w.title:
                    return w
        except Exception:
            continue

    # Second pass: look for normal Chrome windows
    for w in windows:
        try:
            if w.visible and not w.isMinimized and w.width > 200 and w.height > 200:
                if "Incognito" not in w.title:
                    return w
        except Exception:
            continue

    return 

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


smart_search("youtube")