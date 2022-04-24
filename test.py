import pyautogui as py

cont = 940
for i in range(101):
    new = py.locateOnScreen('checkbox.png', confidence=0.7,region=(cont,200,80,900))
    py.click(new)
    new = None
    cont += 2

