from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv_obj=Service('C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

#Capture Cookies from the browser
cookies=driver.get_cookies()
print("Size of cookies:", len(cookies)) #4

#Print details of all cookies
for c in cookies:
    #print(c)
    print(c.get('name'),":",c.get('value'))

#add cookie
driver.add_cookie({"name":"mycookie","value":"1232"})
cookies=driver.get_cookies()
print("Size of Newcookies:", len(cookies)) #5

#Delete cookie
driver.delete_cookie("mycookie")
cookies=driver.get_cookies()
print("Size of cookies after delete:", len(cookies)) #4


#Delete all cookies
driver.delete_all_cookies()









driver.quit()








