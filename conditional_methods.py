from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://olplot.com/login")

email = driver.find_element_by_name("email")

password = driver.find_element_by_name("password")

email.send_keys("wesleyjones752@gmail.com")
password.send_keys("wesley89")

driver.find_elements_by_tag_name("button")[0].click()

print("Regarding name :", email.is_displayed())
print("Regarding name ", email.is_enabled())
print("Regarding password: ", password.is_enabled())
print("Regarding password: ", password.is_displayed())
print(driver.title)

driver.quit()
driver.quit()
