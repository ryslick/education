from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не опустится до $100
    text1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_tag_name("button")
    button.click()


    # копируем число и рассчитываем формулу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = math.log(abs(12*math.sin(int(x))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла