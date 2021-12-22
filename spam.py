


import pyautogui ,time
time.sleep(5)

f = open("act.txt",'r')





for word in f:
    pyautogui.typewrite(word)
    time.sleep(0)
    pyautogui.press("enter")
