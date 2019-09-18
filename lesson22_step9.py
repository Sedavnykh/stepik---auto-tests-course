import os
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Ivan")
    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("petrov@gmail.com")

    filekey = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    filekey.send_keys(file_path)

    submitButton = browser.find_element_by_css_selector("body > div > form > button")
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()


