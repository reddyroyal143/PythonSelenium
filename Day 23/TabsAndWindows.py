import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

# driver.get('https://demo.nopcommerce.com/')
# driver.maximize_window()
# reglink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

#NewTab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")

#New Window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")


