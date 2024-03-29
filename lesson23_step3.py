from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    btn1 = browser.find_element_by_class_name("btn")
    btn1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    num = math.log(abs(12*math.sin(int(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(num))
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

