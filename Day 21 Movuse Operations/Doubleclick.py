import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://qa-practice.netlify.app/double-click')
driver.maximize_window()
button=driver.find_element(By.XPATH,"//button[@id='double-click-btn']")

act=ActionChains(driver)
act.double_click(button).perform()