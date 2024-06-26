from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time, os


script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.binary_location = os.path.expandvars('%LOCALAPPDATA%/Chromium/Application/chrome.exe')
options.add_argument(f'user-data-dir={script_path}/User Data')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--incognito')
options.add_argument('--remote-debugging-port=9222')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)


def cf_bypass():
    result = None
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f'file://{script_path}/test.html')
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[2])
    if driver.title == "dash.stozu.net":
        input('Page load failed, press Enter to continue.')
    time.sleep(2)
    while driver.title == "Just a moment...":
        print('Bypassing cloudflare...')
        time.sleep(2)
    print('Passed check!')
    try:
        WebDriverWait(driver, 120).until(EC.url_to_be('https://dash.stozu.net/earn'))
        result = True
    except TimeoutException:
        input('Timed out! Press Enter to start farm.')
        result = False
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return result


def main(coin_count=0,start_time=time.time()):
    try:
        driver.get('about:blank')
        if cf_bypass():
            print('Auto started! Press Ctrl+C to exit.')
        else:
            print('Script started. Press Ctrl+C to exit.')
        #start_time = time.time()
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
                        cf_bypass()
                        continue
                    driver.refresh()
                    time.sleep(2)
            coin_count += 1
    except KeyboardInterrupt:
        print('Script stopped, exiting...')
    except Exception as e:
        print(f"An error occurred: {e}")
        input('Caught an error! Press Enter restart.')
        driver.switch_to.window(driver.window_handles[0])
        print(f'Restarted, with {coin_count} coins.')
        main(coin_count,start_time)
    run_duration = time.time() - start_time
    print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')
    driver.quit()
    exit()


if __name__ == "__main__":
    main()
