import pyautogui
import time
pyautogui.moveTo(1137,221)
pyautogui.dragTo(1675,243,4)
pyautogui.dragTo(1400,689,4)
pyautogui.dragTo(1137,221,4)
while True:
   print(pyautogui.position())
   time.sleep(0.2)