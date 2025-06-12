import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\royal\\Desktop\\Python\\Day 23\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_base64()


driver.quit()


