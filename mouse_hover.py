from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_id("menu_admin_viewAdminModule")
users_management=driver.find_element_by_id("menu_admin_UserManagement")
users=driver.find_element_by_id("menu_admin_viewSystemUsers")

action=ActionChains(driver)
action.move_to_element(admin).move_to_element(users_management).move_to_element(users).click().perform()

print("test passed")

driver.quit()