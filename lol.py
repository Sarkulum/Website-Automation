import pyautogui
import win32api
import win32con
import time
import sys
import keyboard
import random

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1) # Pauses script for 0.1 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Define pixel coordinates to click
pixel_coords = [(825, 81), (696, 125), (1496, 441), (1419, 582)]

# Check for 'q' keypress continuously
while keyboard.is_pressed('q') == False:

    # Click on each pixel with a 2-second delay between clicks
    for coord in pixel_coords:
        # Move the cursor to the pixel coordinates
        pyautogui.moveTo(coord[0], coord[1])
    
        # Perform a left mouse button click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, coord[0], coord[1], 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, coord[0], coord[1], 0, 0)
    
        # Wait for 2 seconds between clicks
        time.sleep(2)

# Close the script
sys.exit()
