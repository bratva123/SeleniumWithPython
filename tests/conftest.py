# from pyvirtualdisplay import Display
from selenium import webdriver
def oneTimeSetUp():
        opts = webdriver.ChromeOptions()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')

#         display = Display(visible=1)
#         display.start()
        baseURL = "https://letskodeit.teachable.com/"
        print("before webdriver")
        driver = webdriver.Chrome(executable_path='../chromedriver',options=opts)
        print("after webdriver")
        
#         driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



