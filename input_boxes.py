from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Operation performed on a textbox
# How to find how many textbox present on web page
# How to get the status


driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")
driver.current_url()
driver.get("https://www.toolsqa.com/automation-practice-form/")

# how to provide values to a text
driver.find_element(By.NAME, 'firstname').send_keys("Wesley")
driver.find_element(By.ID, 'lastname').send_keys("Jones")
driver.find_element_by_id('datepicker').send_keys("12/08/2019")
status = driver.find_element_by_id('lastname')
print("is text displayed", status)

print(driver.title)

# print(len(input_box))
print("test was successful")

driver.quit()
