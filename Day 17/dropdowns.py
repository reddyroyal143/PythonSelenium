
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

dropcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
dropcountry=Select(dropcountry_ele)

#selecting the options from drop drown

# dropcountry.select_by_visible_text("India")
# dropcountry.select_by_value("10")
# dropcountry.select_by_index(13)

# capture all the options and print

allOptions=dropcountry.options
print("total",len(allOptions))

for opt in allOptions:
    print(opt.text)

# select dropdown from dropdown without using buitin functions
for opt in allOptions:
    if opt.text=="India":
        opt.click()
        break

allOptions=driver.find_elements(By.XPATH,"//select[@id='input-country']/option")
print(len(allOptions))








