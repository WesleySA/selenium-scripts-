from selenium import webdriver

from  selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")


element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action=ActionChains(driver)
action.double_click(element).perform()

print("Test passed")

driver.quit()
