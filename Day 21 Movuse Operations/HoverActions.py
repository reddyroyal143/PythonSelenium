import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('Admin')
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('admin123')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

#find element and save in variable
driver.find_element(By.XPATH,"")
driver.find_element(By.XPATH,"")

#hover

act=ActionChains(driver)
act.move_to_element().move_to_element().click().perform()






