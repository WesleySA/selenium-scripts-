from selenium import webdriver
import time
# from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium.condition").click()
time.sleep(5)


driver.switch_to.default_content()


driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("ConditionRunner").click()
time.sleep(5)

driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[7]").click()
print("test passed")
driver.quit()
