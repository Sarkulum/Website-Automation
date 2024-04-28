from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  631 Y:  520 RGB: ( 91, 203, 143)
#Tile 2 Position: X:  962 Y:  520 RGB: ( 91, 203, 143)
#Tile 3 Position: X:  1291 Y:  520 RGB: ( 91, 203, 143)
#Tile 4 Position: X:  1621 Y:  520 RGB: ( 91, 203, 143)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(631, 520)[1] == 203:
        click(581, 400)
    if pyautogui.pixel(962, 520)[1] == 203:
        click(682, 400)
    if pyautogui.pixel(1291, 520)[1] == 203:
        click(770, 400)
    if pyautogui.pixel(1621, 520)[1] == 203:
        click(869, 400)
