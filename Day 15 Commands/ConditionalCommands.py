from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()

searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print('Status is: ',searchbox.is_displayed())
print('Status is: ',searchbox.is_enabled())

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rd_male.is_selected())
print(rd_male.is_selected())

rd_male.click()
print(rd_male.is_selected())



driver.close()















