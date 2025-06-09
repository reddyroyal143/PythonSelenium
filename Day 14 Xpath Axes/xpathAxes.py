from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
driver.maximize_window()

#Self

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/self::a").text
# print(text_msg)

#parent

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/parent::td").text
# print(text_msg)

#Child

# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/child::td")
# print(len(childs))

#ancestor

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr").text
# print(text_msg)

#decendant

# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/descendant::*")
# print(len(descendants))

#Following

# following=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/following::*")
# print(len(following))

#Following-sibling

# followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/following-sibling::*")
# print(len(followingsiblings))

#Preceding

preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/preceding::*")
print(len(preceding))

#Preceding-sibling

precedingsibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Prudent Corporate Ad')]/ancestor::tr/precedingsibling::*")
print(len(precedingsibling))









driver.close()


