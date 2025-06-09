from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

# driver.get('https://demo.nopcommerce.com/')
# driver.maximize_window()

#ID
# driver.find_element(By.ID,'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Touch Intel Core i7 14 Ultrabook')
#NAME
# driver.find_element(By.NAME,'q').send_keys('Lenovo Thinkpad X1 Carbon Touch Intel Core i7 14 Ultrabook')

#-------Link text and partial link text----------
# driver.find_element(By.LINK_TEXT,'Register').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'ister').click()


#-------multiple elements----
# slider=driver.find_elements(By.CLASS_NAME,'slider-img')
# print(len(slider))
# links=driver.find_elements(By.TAG_NAME,'a')
# print(len(links))

#------customised locators-----

driver.get('https://www.facebook.com/')
driver.maximize_window()

#tag and ID
# driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('abc')             # (or) driver.find_element(By.CSS_SELECTOR,'#email').send_keys('abc')

#Tag and CLass
# driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('abc')    #if we have space, after space value not take. **Tag name is not mandatory

#Tag and Attribute
# driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal-email]').send_keys('abc')

#Tag, class and atrribute
driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal-email]').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal-pass]').send_keys('abc123')






driver.close()







