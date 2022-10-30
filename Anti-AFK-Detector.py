from time import sleep
import keyboard
from random import randint
import base64
import pyautogui
import time
data = "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4" ; data1 = base64.b64decode(data) ; data0 = data1.decode('utf-8')
dat = "Q2xpY2sgdGhlIFJvYmxveCBHYW1lIFdpbmRvdyAmIFByZXNzIHRoZSAnY3RybCcgS2V5IQ==" ; dat1 = base64.b64decode(dat) ; dat0 = dat1.decode('utf-8')
da = "VG8gRXhpdC4gUHJlc3MgdGhlICdhbHQnIEtleS4=" ; da1 = base64.b64decode(da) ; da0 = da1.decode('utf-8')


print(data0) ; print(" ") ; print(dat0) ; print(da0) ; print(" ")
localtime = time.asctime(time.localtime(time.time()))

keyboard.wait('Ctrl')

while 1==1:
    keyboard.press('a')
    sleep(randint(2,10))
    keyboard.release('a')

    keyboard.press('d')
    sleep(randint(2,12))
    keyboard.release('d')

    def shark_movement1():
        shark_movement = randint(1,6)
        if shark_movement == 1:
            keyboard.press('a')
            print("       Player Moved 'Left' As The Shark.")
            sleep(randint(2,10))
            keyboard.release('a')

        if shark_movement == 2:
            keyboard.press('w')
            print("       Player Moved 'Forward' As The Shark.")
            sleep(randint(2,10))
            keyboard.release('w')

        if shark_movement == 3:
            keyboard.press('s')
            print("       Player Moved 'Backward' As The Shark.")
            sleep(randint(2,10))
            keyboard.release('s')

        if shark_movement == 4:
            keyboard.press('d')
            print("       Player Moved 'Right' As The Shark.")
            sleep(randint(2,10))
            keyboard.release('d')
        
        if shark_movement == 5:
            print("       Player Used The 'Speed Special' As The Shark.")
            sleep(randint(1,4))
            keyboard.press_and_release('Space')



    shark_ifso = pyautogui.locateCenterOnScreen('shark.png', confidence=0.8)
    shark_special = pyautogui.locateOnScreen('go.png', confidence=0.8)

    def Shark_1Special():
        shark_movement1()
        
    if shark_ifso != None:
        print("Player Was Selected To Be Shark. - "+ localtime)
        sleep(randint(20,25))
        Shark_1Special()

    if shark_special != None:
        Shark_1Special()
    
    if keyboard.press_and_release('alt'):
        print("Exiting The Script.")
        sleep(3)
        exit()