from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Para navegação web, o selenium precisa do web drive, no google chrome o nome é -> chrome driver, e no firefox -> geckodriver

web = webdriver.Chrome()

# Login hotmail
web.get('https://login.live.com/')
web.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('automacao_teste@hotmail.com')
web.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
web.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('senha123')
sleep(2)
web.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
if web.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[1]'):
    sleep(2)
    web.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
sleep(2)
web.close()
