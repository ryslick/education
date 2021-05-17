from selenium import webdriver
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #вызываем алерт окно
    button = browser.find_element_by_tag_name("button")
    button.click()

    #принимаем конфирм
    confirm = browser.switch_to.alert
    confirm.accept()

    # копируем число и рассчитываем сумму
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = math.log(abs(12*math.sin(int(x))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла