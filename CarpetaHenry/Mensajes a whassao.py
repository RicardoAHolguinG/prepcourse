import pyautogui, webbrowser
from time import sleep
 

webbrowser.open('http-equiv="X-UA-Compatible"')

sleep(5)

for i in range(100):
    pyautogui.typewrite('Good people in the world')
    pyautogui.press('enter')
    
  
  