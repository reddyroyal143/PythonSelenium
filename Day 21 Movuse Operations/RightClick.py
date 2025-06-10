import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
button="xpath of button element"

act=ActionChains(driver)
act.context_click(button).perform()

