import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Log In']").click()
time.sleep(5)
driver.switch_to.alert.accept()
driver.quit()














