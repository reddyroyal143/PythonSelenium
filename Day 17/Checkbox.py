from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()

#1. select specific checkbox
# driver.find_element(By.XPATH,"//label[@for='gender-radio-1']']").click()
#
# #2. select multiple checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#
# #Aprroach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#
# #Approach 2
# for checkbox in checkboxes:
#     checkbox.click()

#3. select multiple checkboxes

# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

#4. select last 2 checkboxes

# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#5. select first 2 checkboxes

# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#6. clearing all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
















