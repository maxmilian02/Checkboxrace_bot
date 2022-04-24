import pyautogui as py
import threading


def Box_Clicker():
    global cont
    for i in range(104):
        new = py.locateOnScreen('checkbox.png',confidence=0.9,region=(cont,200,80,900))
        py.click(new)
        cont += 2

def main():
    cont = 940
    t3 = threading.Thread(target=Box_Clicker)
    t3.start()
    #Box_Clicker()

main()

