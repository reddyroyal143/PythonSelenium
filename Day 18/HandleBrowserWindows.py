import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(10)
# window=driver.current_window_handle
# print(window)

link=(driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']"))
link.click()
windowIDs=driver.window_handles

#Approach1
# parentwindowID=windowIDs[0]
# childwindowID=windowIDs[1]
#
# driver.switch_to.window(childwindowID)
# print("child window ID",driver.title)
#
# driver.switch_to.window(parentwindowID)
# print("child window ID",driver.title)

#Approach2
# for winId in windowIDs:
#     driver.switch_to.window(winId)
#     print(driver.title)

#Approach3
for winId in windowIDs:
    driver.switch_to.window(winId)
    if driver.title=="OrangeHRM":
        driver.close()












# driver.quit()






