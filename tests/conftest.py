from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManage
def oneTimeSetUp():
#         os.chmod('./chromedriver', 755)

#         display = Display(visible=1)
#         display.start()
        baseURL = "https://letskodeit.teachable.com/"
        print("before webdriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("after webdriver")
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



