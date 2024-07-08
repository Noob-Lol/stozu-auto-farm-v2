import time, os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-gpu')
# yay stozu proxy!
options.add_argument("--proxy-server=http://node1.stozu.net:6005")
extensions_path = os.path.expandvars('%LOCALAPPDATA%/Google/Chrome/User Data/Default/Extensions')
required_extensions=['cjpalhdlnbpafiamejdnhcphjbkeiagm','mpbjkejclgfgadiemmefgebjfooflfhl']
# idk what this is but it works
all_extensions = ','.join(os.path.join(extensions_path, ext, os.listdir(os.path.join(extensions_path, ext))[0]) for ext in required_extensions)
options.add_argument(f'--load-extension={all_extensions}')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

ub_filters = '''!Noob filters, website##.element
dash.stozu.net##.elevation-4.sidebar-dark-primary.sidebar-open.main-sidebar
dash.stozu.net##.navbar-light.navbar-dark.navbar-expand.navbar.sticky-top.main-header
dash.stozu.net##.main-footer
dash.stozu.net##.card-body > .row
dash.stozu.net##.swal2-backdrop-show.swal2-top-end.swal2-container
'''
first_run = True
coin_count=0
start_time=0.0

with webdriver.Chrome(options=options) as driver:
    while True:
        try:
            if first_run:
                first_run = False
                driver.get('https://dash.stozu.net/home')
                try:
                    WebDriverWait(driver, 120).until(EC.url_to_be('https://dash.stozu.net/home'))
                    print('Auto started! Press Ctrl+C to exit.')
                except TimeoutException:
                    input('Timed out! Press Enter to start farm.')
                    print('Script started. Press Ctrl+C to exit.')
                driver.minimize_window()
                driver.get("chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/dashboard.html#1p-filters.html")
                time.sleep(1)
                actions = ActionChains(driver)
                actions.send_keys(ub_filters).perform()
                actions.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()
                start_time = time.time()
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
            if "disconnected: not connected to DevTools" in str(e):
                print("Browser was closed. Exiting...")
                break
            elif "net::ERR_PROXY_CONNECTION_FAILED" in str(e):
                input("Proxy error! Press Enter to retry.")
                continue
            else:
                print(f"An error occurred: {e}")
            #input('Caught an error! Press Enter to restart.')
            driver.switch_to.window(driver.window_handles[0])
            driver.get('https://dash.stozu.net/earn/ad')
            driver.minimize_window()
            print(f'Restarted with {coin_count} coins.')
            continue
    if start_time == 0.0:
        print('Script wasnt started.')       
    else:
        run_duration = time.time() - start_time
        print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')
