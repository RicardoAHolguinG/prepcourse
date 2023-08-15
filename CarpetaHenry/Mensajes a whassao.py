import pyautogui, webbrowser
from time import sleep
 

webbrowser.open('https://web.whatsapp.com/send?phone=+Numero de la persona')

sleep(5)

for i in range(101):
    pyautogui.typewrite('Aqui puedes escribir mensajes aleatorios.')
    pyautogui.press('enter')
    
  

  