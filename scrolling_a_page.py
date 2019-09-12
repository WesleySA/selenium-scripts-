from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# scroll page by pixel
driver.execute_script("window.scrollBy(0,1000)", "")

sa = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[68]/td[1]")


# scroll till the element is found
driver.execute_script("arguments[0].scrollIntoView();", sa)

# scroll page until end of  page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

print("Pass test")
driver.quit()
