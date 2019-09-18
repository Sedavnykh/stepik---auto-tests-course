from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    getx = browser.find_element_by_id("input_value")
    x = getx.text
    calc = math.log(abs(12*math.sin(int(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(calc))

    browser.execute_script("window.scrollBy(0, 100);")

    checkboxROB = browser.find_element_by_id("robotCheckbox")
    checkboxROB.click()

    radiobuttonRob = browser.find_element_by_id("robotsRule")
    radiobuttonRob.click()

    submitButton = browser.find_element_by_css_selector("body > div > form > button")
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()
