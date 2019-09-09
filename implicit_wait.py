from  selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")


driver.get('https://marine.olsps.com/')

driver.implicitly_wait(5)
driver.find_element_by_id("menu-item-2755").click()

print(driver.title)
driver.quit()