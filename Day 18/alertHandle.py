import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Welcome")
alertwindow.accept() #OK Button
alertwindow.dismiss() #Cancle button














