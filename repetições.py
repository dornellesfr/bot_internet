from time import sleep
from pip import main
import pyautogui as py
from time import sleep


def repeat(command, n, finish=False):
    n = int(n)
    count = 1
    while count <= n:
        py.press(command)
        count += 1
    if finish:
        py.press(finish)





if __name__ == '__main__':
    repeat('win', '2', 'tab')
