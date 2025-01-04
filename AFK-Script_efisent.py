import pydirectinput
import pyautogui
import keyboard
import time as t
from random import randint as rand
from os import system
from os import path
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False #need this otherwise an exception will be raised(at least on 3.11) - pyautogui stuff

check_win = path.exists("C:\Windows\SysWOW64") # Linux or Windows Detection Basically
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

sleep = t.sleep #CBA to modify all the startup sleep lines but i need time for anti roblox kick

def Load(): # startup Animation
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
  sleep(2) #me no like wait 4 sec >:(
  system(clear)

def keyGet():
    while True:
        if keyboard.is_pressed("Enter"):
            return False
        elif keyboard.is_pressed("Enter + Space"):
            return True



def clickOn(image): # function to click on an image
    pyautogui.moveTo(image)
    x,y = pyautogui.position()
    pydirectinput.click(x,y)

#Load() # show creddits
system(clear)
print("Press 'Enter' To Run The Script OR 'Space+Enter' to run with clicking on chat(1080p only)")
print("Press 'Ctrl' To Exit The Script.")
print(" ")


status = keyGet() # true or false also wait for key

print(f"Started Script. Clicking on chat:{status}")


InitTime = t.time()


while keyboard.is_pressed('Ctrl') != True:

    afk0 = pyautogui.locateCenterOnScreen('_afk0.png', confidence=0.9)
    afk1 = pyautogui.locateCenterOnScreen('_afk1.png', confidence=0.9)
    afk2 = pyautogui.locateCenterOnScreen('_afk2.png', confidence=0.9)
    afk3 = pyautogui.locateCenterOnScreen('_afk3.png', confidence=0.9)
    afk4 = pyautogui.locateCenterOnScreen('_afk4.png', confidence=0.9)
    afk5 = pyautogui.locateCenterOnScreen('_afk5.png', confidence=0.9)
    afk6 = pyautogui.locateCenterOnScreen('_afk01.png', confidence=0.9)
    afk7 = pyautogui.locateCenterOnScreen('_afk6.png', confidence=0.9)

    if afk0 != None:
        clickOn(afk0)

    if afk1 != None:
        clickOn(afk1)

    if afk2 != None:
        clickOn(afk2)

    if afk3 != None:
        clickOn(afk3)

    if afk4 != None:
        clickOn(afk4)

    if afk5 != None:
        clickOn(afk5)

    if afk6 != None:
        clickOn(afk6)

    if afk7 != None:
        clickOn(afk7)

    #counter stuff
    if status == True: 
        if t.time() > InitTime + 900:# check in secs, 15 mins
            for _ in range(5):#to be sure 
                pydirectinput.click(69,35+rand(-3,3))#coords of toggle chat button
            InitTime = t.time() # reset countdown