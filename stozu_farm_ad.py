from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time, os

script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-gpu')
options.add_argument("--proxy-server=http://node1.stozu.net:6005")
# yay stozu proxy!
options.add_extension(f'{script_path}/Violentmonkey.crx')
options.add_extension(f'{script_path}/uBlock-Origin.crx')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

coin_count=0
start_time=0.0
while True:
    try:
        driver.get('https://dash.stozu.net/earn')
        driver.get(f'file://{script_path}/noob-script.user.js')
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        body=driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL,Keys.ENTER)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        try:
            WebDriverWait(driver, 120).until(EC.url_to_be('https://dash.stozu.net/earn'))
            print('Auto started! Press Ctrl+C to exit.')
        except TimeoutException:
            input('Timed out! Press Enter to start farm.')
            print('Script started. Press Ctrl+C to exit.')
        if start_time == 0.0:
            start_time = time.time()
        driver.minimize_window()
        while True:
            driver.get('https://dash.stozu.net/earn/ad')
            time.sleep(10)
            driver.refresh()
            while True:
                try:
                    driver.find_element(By.XPATH, "//h1[text()='Time remaining: 0 seconds']")
                    break
                except NoSuchElementException:
                    if driver.title != "Stozu - Free":
                        if driver.title == "dash.stozu.net":
                            input('Connection error, press Enter to continue.')
                        else:
                            input('Unhandled error, pls check window.')
                    driver.refresh()
                    time.sleep(2)
                    try:
                        driver.find_element(By.XPATH, "//h1[text()='Time remaining:  seconds']")
                        break
                    except NoSuchElementException:
                        pass
            coin_count += 1
    except KeyboardInterrupt:
        print('Script stopped, exiting...')
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        input('Caught an error! Press Enter restart.')
        driver.switch_to.window(driver.window_handles[0])
        print(f'Restarted, with {coin_count} coins.')
        continue
if start_time == 0.0:
    print('Script wasnt started.')       
else:
    run_duration = time.time() - start_time
    print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')
driver.quit()
