from base.selenium_driver import SeleniumDriver
import utilities.customLogger as cl
import logging
import  time

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        time.sleep(2)

        self.elementClick("//a[contains(text(),'Login')]", locatorType="xpath")
        # print("befor login click")
        # self.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        # print("befor login click")

    def enterEmail(self, email):
        self.waitForElement(self._email_field)
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # time.sleep(5)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[contains(text(),'My Courses')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]",
                                       locatorType="xpath")
        return result

