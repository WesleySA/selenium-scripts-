from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_elements_by_tag_name("button")[0].click()

time.sleep(5)

# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

print("test passed")
