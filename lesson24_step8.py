from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()

    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    num = math.log(abs(12*math.sin(int(x))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(num))
    buttn = browser.find_element_by_id("solve")
    buttn.click()

finally:
    time.sleep(10)
    browser.quit()
