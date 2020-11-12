from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile 1 = X:  582 Y:  724 RGB: (163, 159, 227)
#tile 2 = X:  678 Y:  731 RGB: (163, 159, 227)
#tile 3 = X:  783 Y:  737 RGB: (171, 166, 230)
#tile 4 = X:  876 Y:  733 RGB: (173, 169, 229)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(589,600)[0] ==0:
        click(589,600)
    if pyautogui.pixel(690,600)[0] ==0:
        click(690,600)
    if pyautogui.pixel(779,600)[0] ==0:
        click(779,600)
    if pyautogui.pixel(864,600)[0] ==0:
        click(864,600)

