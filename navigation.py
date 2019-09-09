from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.inc.com")  # first application opened

print("This is the first app opened :", driver.title)

driver.get("https://quire.io/")
driver.back()

driver.forward()
print("this is the second app opened: ", driver.title)
driver.quit()
