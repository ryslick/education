from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #вызываем алерт окно
    button = browser.find_element_by_tag_name("button")
    button.click()

    #переключаемся на новую вкладку
    window_before = browser.window_handles[0]
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)


    # копируем число и рассчитываем формулу
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