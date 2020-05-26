from selenium import webdriver
from pyvirtualdisplay import Display
import os

def oneTimeSetUp():
#         chrome_options = webdriver.ChromeOptions()
# #         Display(visible=1, size=(1000, 1000)).start()
#         chrome_options.add_argument('--disable-extensions')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
        
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('window-size=1920x1080')
        # driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')
        driver = webdriver.Firefox(options=option)
        baseURL = "https://letskodeit.teachable.com/"
        driver.get(baseURL)
        print("Running tests on firefox")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



