from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("div .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("#robotcheckbox")
    input2.click()
    input3 = browser.find_element_by_css_selector("#robotsrule")
    input3.click()



    # Отправляем заполненную форму

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
