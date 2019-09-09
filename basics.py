from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.inc.com/")

print('this is the title of the page ' + driver.title)

driver.find_element_by_css_selector(
    "#TopNav > nav > div.inner-container.container-fluid > div.navbar-header > button").click()

time.sleep(5)
driver.close()
