from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

browser = None
try:
    browser = webdriver.Chrome(options=chrome_options)
    
    # browser.get("http://suninjuly.github.io/registration1.html")
    
    browser.get("http://suninjuly.github.io/registration2.html")
    
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("test@test.com")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Тест успешно пройден!")

except Exception as e:
    print(f"Произошла ошибка: {e}")
    import traceback
    traceback.print_exc()

finally:
    if browser:
        time.sleep(2)
        browser.quit()
