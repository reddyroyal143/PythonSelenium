import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://practice-automation.com/iframes/')
driver.maximize_window()

driver.switch_to.frame("bottom-iframe")
driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']")

driver.switch_to.default_content()

driver.find_element(By.XPATH,"//img[contains(@alt,'automateNow Logo')]")






