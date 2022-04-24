import pyautogui as py
from time import sleep

#but = py.locateAllOnScreen('check2.png', confidence=0.9)
#print(but)


'''
region=(940,540,45,44)
        943 538 45 44
        946 549 45 44
        946 527 45 44
        969 509 45 44
        977 494 45 44
        980 488 45 44
        984 476 45 44
        988 591 45 44
''''''
for i in range(930,990):
    x = i
    for j in range(470,600):
        y = j
        but = py.locateOnScreen('check2.png', confidence=0.9,region=(940,350,45,500))
        print(x,y)
        if but != None:
            py.moveTo(but)
            break
'''
cont = 940
while True:
    but = py.locateOnScreen('check2.png', confidence=0.85,region=(cont,200,80,900))
    if but != None:
        py.click(but)
        cont += 2
        print(cont)
    else:
        break
    

