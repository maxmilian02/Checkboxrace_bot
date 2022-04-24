import pyautogui as py
from time import perf_counter as pf

code_start = pf()
range1 = 100
cont = 940
for i in range(104):
    new = py.locateOnScreen('checkbox.png', confidence=0.9,region=(cont,200,80,900))
    py.click(new)
    new = None
    cont += 2

print(f'Code ended in {code_start} seconds')

