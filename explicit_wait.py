import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

print(driver.title)
driver.find_element(By.ID, "package-origin-hp-package").send_keys("SFO")  # origin

time.sleep(5)

driver.find_element(By.ID, "package-destination-hp-package").send_keys("NYC")  # destination

driver.find_element(By.ID, "package-departing-hp-package").clear()
driver.find_element(By.ID, "package-departing-hp-package").send_keys("12/10/2019")  # departing

driver.find_element(By.ID, "package-returning-hp-package").clear()
driver.find_element(By.ID, "package-returning-hp-package").send_keys("15/10/2019")  # returning

driver.find_element_by_id("search-button-hp-package").click()

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.ID, "star3")))

element.click()

time.sleep(5)  # from python

driver.quit()
