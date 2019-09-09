from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

"""Objectives :
1) How to find put how many link are present?
2) How to capture links
3) How to click on links
"""
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

links = driver.find_elements_by_tag_name("a")

for link in links:
    print(link.text)

driver.implicitly_wait(10)
driver.find_element_by_link_text("Interview Prep").click()

print("number of links", len(links))

print("test passed")
driver.quit()
