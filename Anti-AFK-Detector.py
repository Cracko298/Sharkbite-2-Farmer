from time import sleep
import keyboard
from random import randint
import base64
import pyautogui
import time
data = "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4" ; data1 = base64.b64decode(data) ; data0 = data1.decode('utf-8') ; keypress = 'alt'
dat = "Q2xpY2sgdGhlIFJvYmxveCBHYW1lIFdpbmRvdyAmIFByZXNzIHRoZSAnY3RybCcgS2V5IQ==" ; dat1 = base64.b64decode(dat) ; dat0 = dat1.decode('utf-8')
da = "VG8gRXhpdC4gUHJlc3MgdGhlIGFuZCBob2xkICdhbHQnIEtleS4gKEFmdGVyIHlvdSBoZXJlIGEgbm90aWZpY2F0aW9uIHNvdW5kIFByZXNzICdhbHQnIHR3aWNlKS4=" ; da1 = base64.b64decode(da) ; da0 = da1.decode('utf-8')


print(data0) ; print(" ") ; print(dat0) ; print(da0) ; print(" ")
localtime = time.asctime(time.localtime(time.time()))

keyboard.wait('Ctrl')

while keyboard.read_key() != "alt":
    subconf = pyautogui.locateCenterOnScreen('subconfirm.png', confidence=0.55)
    under0 = pyautogui.locateCenterOnScreen('underwater.png', confidence=0.55)
    under1 = pyautogui.locateCenterOnScreen('under.png', confidence=0.55)
    under2 = pyautogui.locateCenterOnScreen('darkestwat.png', confidence=0.55)
    under3 = pyautogui.locateCenterOnScreen('darkhill.png', confidence=0.55)
    under4 = pyautogui.locateCenterOnScreen('darkwat.png', confidence=0.55)
    under5 = pyautogui.locateCenterOnScreen('lightestwat.png', confidence=0.55)
    under6 = pyautogui.locateCenterOnScreen('lightwat.png', confidence=0.55)
    keyboard.press_and_release('Ctrl')


    def Sub_Movement():
        keyboard.press_and_release('Ctrl')
        global subconf
        keyboard.press('q')
        sleep(randint(3,6))
        keyboard.release('q')
        keyboard.press('e')
        sleep(randint(3,6))
        keyboard.release('e')

    keyboard.press('a')
    sleep(randint(2,8))
    keyboard.release('a')
    keyboard.press('d')
    sleep(randint(2,7))
    keyboard.release('d')

    if subconf != None:
        Sub_Movement()
    if under0 != None:
        Sub_Movement()
    if under1 != None:
        Sub_Movement()
    if under2 != None:
        Sub_Movement()
    if under3 != None:
        Sub_Movement()
    if under4 != None:
        Sub_Movement()
    if under5 != None:
        Sub_Movement()
    if under6 != None:
        Sub_Movement()

    if subconf != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under0 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under1 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under2 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under3 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under4 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under5 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
        keyboard.release('d')

    if under6 != True:
        keyboard.press_and_release('Ctrl')
        keyboard.press('a')
        sleep(randint(2,8))
        keyboard.release('a')
        keyboard.press('d')
        sleep(randint(2,7))
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



    shark_ifso = pyautogui.locateCenterOnScreen('shark.png', confidence=0.55)
    shark_special = pyautogui.locateOnScreen('go.png', confidence=0.55)
    ducksubmarine = pyautogui.locateCenterOnScreen('ducksub.png', confidence=0.55)
    militarymarine = pyautogui.locateCenterOnScreen('milsub.png', confidence=0.55)

    if militarymarine != None:
        print("Player Used 'Military Submarine' as Submarine. - "+ localtime)
        sleep(randint(10,14))
        Sub_Movement()
    
    if ducksubmarine != None:
        print("Player Used 'Duckmarine' as Submarine. - "+ localtime)
        sleep(randint(10,14))
        Sub_Movement()

    def Shark_1Special():
        shark_movement1()
        
    if shark_ifso != None:
        print("Player Was Selected To Be Shark. - "+ localtime)
        sleep(randint(20,25))
        Shark_1Special()

    if shark_special != None:
        Shark_1Special()

exit()