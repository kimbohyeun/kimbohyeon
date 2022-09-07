import pyautogui
import time
#google을 들어간 처음 화면이고 화면을 윈도우 오른쪽 화살표로 띄어
#놓을것
pyautogui.moveTo(1257,209,0.8)
pyautogui.click()
#한영키를 한글로 해 놓을것
pyautogui.typewrite("dhgusrhemdgkrry rhdtlrghavpdlwl")
pyautogui.moveTo(1785,205,0.8)
pyautogui.click()
pyautogui.moveTo(1175,622,0.8)
pyautogui.click()
pyautogui.moveTo(1787,825,0.8)
pyautogui.click()
pyautogui.moveTo(1903,104,0.8)
pyautogui.dragTo(1903,804,6)
pyautogui.dragTo(1903,104,2)
pyautogui.moveTo(1441,604,0.8)
pyautogui.click()
pyautogui.moveTo(1903,104,0.8)
pyautogui.dragTo(1903,804,6)
pyautogui.dragTo(1903,104,2)
while True:
   print(pyautogui.position())
   time.sleep(0.2)