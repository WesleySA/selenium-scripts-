from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

element = driver.find_element_by_id("continents")

drb = Select(element)

for o in drb.options:
    print(o.text)

    print(len(drb.options))

drb.select_by_visible_text("South America")

print("test passed")

driver.quit()
