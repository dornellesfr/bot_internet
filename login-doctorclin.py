from webbrowser import Chrome
import pyautogui
from time import sleep
# Login doctorclin

# Abrir o google chrome
# Abrir o site "https://app2.goclin.com/"
# Clicar e preencher login e senha

pyautogui.PAUSE = 0.5
pyautogui.alert('O CÓDIGO VAI COMEÇAR, NÃO MEXA EM NADA!')
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(1)
pyautogui.write('https://app2.goclin.com/')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('uniclinesteio@gmail.com')
pyautogui.press('tab')
pyautogui.write('uniesteio01')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')