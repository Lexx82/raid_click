import pyautogui as pg
import time


def bAgain():
    location = pg.locateOnScreen('again.png')
    point = pg.center(location)
    x, y = point
    pg.click(x, y)


while 1:
    try:
        bAgain()
    except:
        time.sleep(5)
