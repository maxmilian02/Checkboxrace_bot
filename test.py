import pyautogui as py

cont = 940
old = 0
error_count = 0
steps = 0
for i in range(101):
    new = py.locateOnScreen('checkbox.png', confidence=0.7,region=(cont,200,80,900))
    if new == old:
        error_count += 1
        py.screenshot(f'error_{error_count}_step_{steps}.png',region=(cont,200,80,900))
        print(f'Error1: cant find image on screen. Times ocurred:{error_count}')
        print(f'Error occured in {new}')
    else:
        py.click(new)
        steps += 1
        new = None
    old = new
    cont += 2

