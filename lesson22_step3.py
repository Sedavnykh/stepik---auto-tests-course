from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num11 = num1.text
    num2 = browser.find_element_by_id("num2")
    num22 = num2.text
    sum = str(int(num11) + int(num22))
    choose = Select(browser.find_element_by_id("dropdown"))
    choose.select_by_visible_text(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


