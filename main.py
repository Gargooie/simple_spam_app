import pyautogui,time

time.sleep(5)
file=open("text.txt","r")

for x in file:
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(0.5)
