# from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManage
def oneTimeSetUp():
        opts = webdriver.ChromeOptions()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
        opts.add_argument("--headless")
        opts.add_argument("--incognito")
#         os.chmod('./chromedriver', 755)

#         display = Display(visible=1)
#         display.start()
        baseURL = "https://letskodeit.teachable.com/"
        print("before webdriver")
        driver = webdriver.Chrome(options=opts,ChromeDriverManager().install())
        print("after webdriver")
        
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



