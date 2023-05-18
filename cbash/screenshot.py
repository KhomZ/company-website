import pyautogui
import time

i = 0
while(i < 10):
    img = pyautogui.screenshot()
    img.save("cbash\shot"+str(i)+".png")
    i = i+1
    time.sleep(2)