from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button_1 = browser.find_element(By.ID, "book").click()


    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    print(input)
    input.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:

    time.sleep(10)
    browser.quit()

