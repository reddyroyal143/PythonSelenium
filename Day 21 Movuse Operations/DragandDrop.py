import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.automationtesting.in/Static.html')
driver.maximize_window()
time.sleep(5)

source=driver.find_element(By.XPATH,"//div[@class='col-xs-10 col-xs-offset-2']//img[@id='angular']")
target=driver.find_element(By.XPATH,'//*[@id="droparea"]')

act=ActionChains(driver)
act.drag_and_drop(source,target)



