from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.toolsqa.com/automation-practice-form/?firstname=&submit=&photo=&continents=AS")

# How to work with radio button


driver.find_element_by_id('cookie_action_close_header').click()

driver.implicitly_wait(10)

driver.find_element_by_id('sex-0').click()
status = driver.find_element_by_id('sex-0').is_selected()
driver.find_element_by_id('sex-1').is_selected()
female = driver.find_element_by_id('sex-1').click()
print("male status", status)
print("female status", female)
driver.quit()

# print(status)
