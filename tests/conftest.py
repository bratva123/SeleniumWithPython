from selenium import webdriver
# from pyvirtualdisplay import Display

def oneTimeSetUp():
        chrome_options = webdriver.ChromeOptions()
#         Display(visible=1, size=(1000, 1000)).start()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        baseURL = "https://letskodeit.teachable.com/"
        print("before webdriver")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        print("after webdriver")
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



