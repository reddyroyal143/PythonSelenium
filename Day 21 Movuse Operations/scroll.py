#Approach1-scroll down page by pixel

# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("returnwindow.pageYOffse;")
# print(value)

#2 scrolling till the element

#find element and store in variable(flag)
#driver.execute_script("arguments[0].scroolIntoView();",flag)
# value=driver.execute_script("returnwindow.pageYOffse;")
# print(value)

#3 scroll till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
# value=driver.execute_script("returnwindow.pageYOffse;")
# print(value)

#4 scroll till top
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
# value=driver.execute_script("returnwindow.pageYOffse;")
# print(value)

