from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.w3schools.com/python/python_comments.asp")
driver.find_element_by_link_text("Run example »").click()

print(driver.current_window_handle)

handles = driver.window_handles
#
# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)

print("passed test")
driver.quit()
