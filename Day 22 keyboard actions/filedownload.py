import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():

    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Users/royal/Desktop/Drivers/chromedriver-win64/chromedriver.exe")
    #download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome (service=serv_obj,options=ops)
    return driver

def edge_setup():

    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Users/royal/Desktop/Drivers/edgedriver_win64/msedgedriver.exe")
    #download files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge (service=serv_obj,options=ops)
    return driver


def firefox_setup():

    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Users/royal/Desktop/Drivers/edgedriver_win64/msedgedriver.exe")
    #settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2) #0 is desktop, 1 is default, 2 is desired location
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox (service=serv_obj)
    return driver

#Automation code
driver=chrome_setup()
driver=edge_setup()
driver=firefox_setup()



driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()