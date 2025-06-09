import time
from selenium import webdriver

#C:\Users\royal\AppData\Local\Programs\Python\Python313\Scripts  ----- put drivers in this folder

#selenium 3
#-------------------
# driver=webdriver.Chrome("C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
#
# time.sleep(20)
#
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#
# act_title=driver.title
# exp_title='OrangeHRM'
#
# if act_title==exp_title:
#     print('Login Test Passed')
# else:
#     print('Login test failed')
#
# driver.close()

#Selenium 4
#--------------------------

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

#driver=webdriver.Chrome() -----------  use if u have drivers in python folder
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(10)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

act_title=driver.title
exp_title='OrangeHRM'

if act_title==exp_title:
    print('Login Test Passed')
else:
    print('Login test failed')

driver.close()















