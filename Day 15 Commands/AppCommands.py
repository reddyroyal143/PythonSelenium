from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(driver.title)
print(driver.current_url)
print(driver.page_source)  #used rarely

driver.close()



