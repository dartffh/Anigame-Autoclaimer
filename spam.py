import requests
import time
from PIL import Image
import pyautogui
from pytesseract import pytesseract
from datetime import datetime
from colorama import init,Fore,Back,Style
import os


pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
init(convert=True)

Commons = 0
Uncommons = 0
Rares = 0
SuperRares = 0
UltraRares = 0
LotteryStartTime = datetime.now().strftime("%H%M")
HourlyStartTime = datetime.now().strftime("%H%M")
message = pyautogui.locateOnScreen("Message.PNG", grayscale=True, confidence=.9)

############################################################################################################################################################

def wasgefunden():
    #Checking for the Card we got
    print("")
    time.sleep(1)
    left, top, width, height = 596, 1900, 1000, 30
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    box = (left,top,left + width, top + height)
    region = screenshot.crop(box)
    text = pytesseract.image_to_string(region)
    time.sleep(1)
    common = pyautogui.locateOnScreen("Common.PNG", grayscale=True, confidence=.9)
    Uncommon = pyautogui.locateOnScreen("Uncommon.PNG", grayscale=True, confidence=.9)
    Rare = pyautogui.locateOnScreen("Rare.PNG", grayscale=True, confidence=.9)
    SuperRare = pyautogui.locateOnScreen("SuperRare.PNG", grayscale=True, confidence=.9)
    if common is not None:
        print(text)
        global Commons
        Commons = Commons + 1
    if Uncommon is not None:
        print(Fore.GREEN + text + Style.RESET_ALL)
        global Uncommons
        Uncommons = Uncommons + 1
    if Rare is not None:
        print(Fore.BLUE + text + Style.RESET_ALL)
        global Rares
        Rares = Rares + 1
    if SuperRare is not None:
        print(Fore.YELLOW + text + Style.RESET_ALL)
        print(text)
        global SuperRares
        SuperRares = SuperRares + 1

    #Deleting the message to avoid confusing the Bot
    pyautogui.click(button='right')
    time.sleep(0.2)
    deletor = pyautogui.locateOnScreen("Delete.PNG", grayscale=True, confidence=.9)
    pyautogui.moveTo(deletor)
    time.sleep(1)
    pyautogui.click()
    pyautogui.press('enter')
    Result()
    Main()


############################################################################################################################################################
    
def Main():
    
    payload = {
        'content': 'a'
    }

    header = {
        'authorization': ''
    }
    message = pyautogui.locateCenterOnScreen("Unbenannt.PNG", grayscale=True, confidence=.8)
    r = requests.post('https://discord.com/api/v9/channels/1074342717074722819/messages', data=payload, headers = header)
    res = pyautogui.locateCenterOnScreen("Unbenannt.PNG", grayscale=True, confidence=.8)
    if res is not None:
        pyautogui.moveTo(res)
        pyautogui.click()
        wasgefunden()

############################################################################################################################################################

def TitleScreen():
    os.system('cls')
    print(Fore.RED + "  _    _ _ _   _                 _                        _                              ____        _   ")
    print(" | |  | | | | (_)               | |           /\         (_)                            |  _ \      | |  ")
    print(" | |  | | | |_ _ _ __ ___   __ _| |_ ___     /  \   _ __  _  __ _  __ _ _ __ ___   ___  | |_) | ___ | |_ ")
    print(" | |  | | | __| | '_ ` _ \ / _` | __/ _ \   / /\ \ | '_ \| |/ _` |/ _` | '_ ` _ \ / _ \ |  _ < / _ \| __|")
    print(" | |__| | | |_| | | | | | | (_| | ||  __/  / ____ \| | | | | (_| | (_| | | | | | |  __/ | |_) | (_) | |_ ")
    print("  \____/|_|\__|_|_| |_| |_|\__,_|\__\___| /_/    \_\_| |_|_|\__, |\__,_|_| |_| |_|\___| |____/ \___/ \__|")
    print("                                                             __/ |                                       ")
    print("                                                            |___/                                        " + Style.RESET_ALL)
    print("")
    print("")

############################################################################################################################################################

def Result():
    global Commons
    global Uncommons
    global Rares
    global SuperRares
    global UltraRares
    print(Fore.RED + "So far you have found: " + Style.RESET_ALL)
    print("Commons: " + str(Commons))
    print(Fore.GREEN + "Uncommons: " + str(Uncommons) + Style.RESET_ALL)
    print(Fore.BLUE + "Rares: " + str(Rares) + Style.RESET_ALL)
    print(Fore.YELLOW + "Super Rares: " + str(SuperRares) + Style.RESET_ALL)
    print(Fore.MAGENTA + "Ultra Rares: " + str(UltraRares) + Style.RESET_ALL)
    Main()

############################################################################################################################################################

TitleScreen()
print(Fore.GREEN + "Starting the Bot..." + Style.RESET_ALL)
time.sleep(5)
print(Fore.GREEN + "Started Succesfully!" + Style.RESET_ALL)

pyautogui.write(".lottery")
pyautogui.press('enter')
pyautogui.write(".hourly")
pyautogui.press('enter')
print("")
print("")
print("")
print(Fore.BLUE + "Lottery Executed Succesfully")
print("Hourly Executed Succesfully!" + Style.RESET_ALL)
print("")
print("")
print("")



while (True):
    newtime = datetime.now().strftime("%H%M")
    if int(newtime) - int(LotteryStartTime) >= 11:
        pyautogui.moveTo(message)
        pyautogui.click()
        pyautogui.write(".lottery")
        pyautogui.press('enter')
        print(Fore.BLUE + "Lottery Executed Succesfully" + Style.RESET_ALL)
        LotteryStartTime = newtime
    
    if int(newtime) - int(HourlyStartTime) >=61:
        pyautogui.moveTo(message)
        pyautogui.click()
        pyautogui.write(".hourly")
        pyautogui.press('enter')
        print(Fore.BLUE + "Hourly Executed Succesfully!" + Style.RESET_ALL)
        HourlyStartTime = newtime
    time.sleep(0.1)
    Main()
