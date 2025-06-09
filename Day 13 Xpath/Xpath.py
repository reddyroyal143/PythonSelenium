from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('')
driver.maximize_window()

#Absolute Xpath


#Relative Xpath

#Or operator

#and operator

#contains() and starts-with() --- important for dynamic elements

#text()














