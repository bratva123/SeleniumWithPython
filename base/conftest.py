from pyvirtualdisplay import Display
from selenium import webdriver
import os
from py._xmlgen import html
def oneTimeSetUp():
        # display = Display(visible=1, size=(1024, 768))
        # display.start()
        # # chrome_options = webdriver.ChromeOptions()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('window-size=1920x1080')
        # # chrome_options.add_argument("--disable-extensions")
        # # chrome_options.add_argument("--proxy-server='direct://'")
        # # chrome_options.add_argument("--proxy-bypass-list=*")
        # chrome_options.add_argument("--start-maximized")
        # # chrome_options.add_argument('--headless')
        # # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--no-sandbox')
        # # chrome_options.add_argument('--ignore-certificate-errors')
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('window-size=1920x1080')
        # os.chmod('./geckodriver',777)
        baseURL = "https://letskodeit.teachable.com/"
        # driver = webdriver.Chrome(options=opts)
        # driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')
        driver = webdriver.Firefox(options=option)
        driver.set_window_size(1000, 1000)
        driver.get(baseURL)
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



