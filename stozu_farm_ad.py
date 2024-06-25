from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time, random, os
script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.binary_location = os.path.expandvars('%LOCALAPPDATA%/Chromium/Application/chrome.exe')
options.add_argument(f'user-data-dir={script_path+'/User Data'}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--incognito')
options.add_argument('--remote-debugging-port=9222')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
start_time = time.time()

#code starts here
try:
    driver.get(f'file://{script_path+'/test.html'}')
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])

#after passing clouflare check and logging in
    input('Press Enter to start farm...')
    start_time = time.time()
    coin_count = 0
    print('Script started, press Ctrl+C to exit')
    driver.minimize_window()
    while True:
        driver.get('https://dash.stozu.net/earn/ad')
        time.sleep(10)
        time.sleep(random.uniform(0, 2))
        driver.refresh()
        while True:
            try:
                driver.find_element(By.XPATH, "//h1[text()='Time remaining: 0 seconds']")
                break
            except NoSuchElementException:
                if driver.title == "Just a moment...":
                    time.sleep(5)
                    print('stuck on cloudflare')
                    continue
                driver.refresh()
                time.sleep(2)
        coin_count += 1
except KeyboardInterrupt:
    print('Script stopped, exiting...')
except Exception as e:
    print('got error:'+e)
    input('caught an error, press enter to exit')
    #need to implement continuing

run_duration = time.time() - start_time
print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')
driver.quit()