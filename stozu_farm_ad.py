from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import os
script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.binary_location = os.path.expandvars('%LOCALAPPDATA%/Chromium/Application/chrome.exe')
options.add_argument(f'user-data-dir={script_path+'/User Data'}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--incognito')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

#code starts here
driver.get(f'file://{script_path+'/test.html'}')
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])

#after passing clouflare check and logging in
try:
    input('Press Enter to start farm...')
    start_time = time.time()
    coin_count = 0
    print('Script started, press Ctrl+C to exit')
    driver.minimize_window()
    while True:
        driver.get('https://dash.stozu.net/earn/ad')
        time.sleep(4)
        while True:
            try:
                button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn btn-primary btn-lg') and text()='Get Coins']")
                button.click()
                break
            except NoSuchElementException:
                driver.refresh()
                time.sleep(2)
        WebDriverWait(driver, 15).until(EC.url_to_be('https://dash.stozu.net/earn'))
        coin_count += 1
except KeyboardInterrupt:
    run_duration = time.time() - start_time
    print('Script stopped, exiting...')
    driver.quit()
    print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')