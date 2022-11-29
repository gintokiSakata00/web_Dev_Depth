import pyautogui
import time
message = ["charles", "bakit", "ang gwapo ko"]
for i in message:
    time.sleep(1)
    pyautogui.typewrite(i)
    pyautogui.press('enter')
  
    