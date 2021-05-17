from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    # копируем числа и рассчитываем сумму
    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
    y = int(x1) + int(x2)
    print(y)

    # находим выпадающее меню и выбираем результат вычесления
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
