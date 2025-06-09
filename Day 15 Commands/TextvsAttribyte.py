from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
username=driver.find_element(By.XPATH,"//input[@id='Email']")

username.clear()

username.send_keys("qwe@gmail.com")

print("Result of Text: ",username.text)
print("Result of get_attribute: ",username.get_attribute('value'))

driver.close()

