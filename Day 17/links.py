from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()


#click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#finding links in a page
# links=driver.find_elements(By.XPATH,'//a')
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))

#print all links
for link in links:
    print(link.text)









driver.quit()







