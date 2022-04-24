import pyautogui as py

cont = 940
old = 0
error_count = 0
for i in range(104):
    new = py.locateOnScreen('checkbox.png', confidence=0.7,region=(cont,200,80,900))
    if new == old:
        error_count += 1
        print(f'Error1: cant find image on screen. Times ocurred:{error_count}')
        print(f'Error occured in {new}')
    else:
        py.click(new)
    old = new
    cont += 2

