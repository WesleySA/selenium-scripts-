from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\wesley\Desktop\webdriver\chromedriver.exe")

driver.get("https://www.toolsqa.com/automation-practice-table/")

row = len(driver.find_elements_by_xpath("//*//*[@id='content']/table/tbody/tr[1]/td"))
column = len(driver.find_elements_by_xpath("//*[@id='content']/table/thead/tr/th"))

print(f"no. of {row}")
print(f"no. of {column}")

print("Check output")
for r in range(1,row+1):
    for c in range(1,column+1):
        value = driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        #//*[@id="content"]/table/tbody/tr[1]/td[1]

        print(value)
        time.sleep(5)

        print("test passed")
        driver.quit()
