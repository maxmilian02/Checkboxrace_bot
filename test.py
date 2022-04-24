import pyautogui as py

cont = 940
while True:
    but = py.locateOnScreen('checkbox.png', confidence=0.85,region=(cont,200,80,900))
    if but != None:
        py.click(but)
        cont += 2
        print(cont)
    else:
        break
    

