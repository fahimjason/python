# print("Hello World")
# print("2+5")
# print('Welcome to my frist python code')

# course = "   python programming"
# print(len(course))
# print(course[0:3])
# print(course[0:])
# print(course[:])
# print(course[:3])

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("pro" not in course)


# from selenium import webdriver
# import time
# from webdriver_manager.chrome import ChromeDriverManager

# def my_function():
#     try:
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         # driver = webdriver.Chrome()
#         driver.get("http://google.com")
#         time.sleep(60)
#         driver.quit()
#     except:
#         print('error')
# my_function()


# https://medium.com/analytics-vidhya/simple-whatsapp-automation-using-python3-and-selenium-77dad606284b
# source venv/Scripts/activate

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

contact = "Dipanjal Bhai"
text = "Hey, this message was sent using Selenium"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(driver, 50).until(
    lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)

driver.quit()
