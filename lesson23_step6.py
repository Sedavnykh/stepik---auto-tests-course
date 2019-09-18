from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_class_name('trollface')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    num = math.log(abs(12*math.sin(int(x))))
    inp = browser.find_element_by_id("answer")
    inp.send_keys(str(num))

    button1 = browser.find_element_by_class_name("btn")
    button1.click()


finally:
    time.sleep(10)
    browser.quit()

