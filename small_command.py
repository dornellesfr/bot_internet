import pyautogui as py

def p(key):
    return py.press(key)


def w(string):
    return py.write(string)


if __name__ == '__main__':
    p('win')
    w('login')
