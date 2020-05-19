from selenium import webdriver
def oneTimeSetUp():
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.maximize_window()
        print("Running tests on chrome")
        return driver

        # yield driver
        # driver.quit()
        # print("Running one time tearDown")



