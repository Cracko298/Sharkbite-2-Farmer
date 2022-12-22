import pydirectinput
import pyautogui
import keyboard
from time import sleep
from os import system
from os import path

check_win = path.exists("C:\Windows\SysWOW64") # Linux or Windows Detection Basically
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

def Load(): # Loading Animation
  sleep(1)
  print("Created By:  r       ")
  sleep(0.15)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.15)
  system(clear)
  print("Created By: Cracko298")
  sleep(4)
  system(clear)

Load()
system(clear)
print("Press 'Enter' To Run The Script.")
print("Press 'Ctrl' To Exit The Script.")
print(" ")

keyboard.wait('Enter')
print("Started Script...")

while keyboard.is_pressed('Ctrl') != True:

    afk0 = pyautogui.locateCenterOnScreen('_afk0.png', confidence=0.9)
    afk1 = pyautogui.locateCenterOnScreen('_afk1.png', confidence=0.9)
    afk2 = pyautogui.locateCenterOnScreen('_afk2.png', confidence=0.9)
    afk3 = pyautogui.locateCenterOnScreen('_afk3.png', confidence=0.9)
    afk4 = pyautogui.locateCenterOnScreen('_afk4.png', confidence=0.9)
    afk5 = pyautogui.locateCenterOnScreen('_afk5.png', confidence=0.9)
    afk6 = pyautogui.locateCenterOnScreen('_afk01.png', confidence=0.9)

    if afk0 != None:
        pyautogui.moveTo(afk0)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)
    
    if afk1 != None:
        pyautogui.moveTo(afk1)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)

    if afk2 != None:
        pyautogui.moveTo(afk2)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)

    if afk3 != None:
        pyautogui.moveTo(afk3)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)

    if afk4 != None:
        pyautogui.moveTo(afk4)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)

    if afk5 != None:
        pyautogui.moveTo(afk5)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)

    if afk6 != None:
        pyautogui.moveTo(afk6)
        x,y = pyautogui.position()
        pydirectinput.moveTo(x+5,y)
        pydirectinput.click(x,y)