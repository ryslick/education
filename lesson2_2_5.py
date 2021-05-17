from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # копируем числ
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    #высчитываем нужное значение
    y = str(math.log(abs(12*math.sin(x))))

    #отправляем значение в форму
    last = browser.find_element_by_id("answer")
    last.send_keys(y)

    #активируем чекбокс и переключаем радиокнопку
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    # Скролируем и Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
