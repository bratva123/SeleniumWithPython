# from pyvirtualdisplay import Display
from selenium import webdriver
def oneTimeSetUp():

#         display = Display(visible=1)
#         display.start()
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path=r"/home/global/Downloads/chromedriver")
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



