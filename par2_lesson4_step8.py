from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    browser.find_element_by_id("book").click()
    
    number = browser.find_element_by_id("input_value").text
    answer = calc(number)

    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("solve").click()

finally:    
    time.sleep(10)
    browser.quit()
