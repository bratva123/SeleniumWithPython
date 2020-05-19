from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from tests.conftest import oneTimeSetUp

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = oneTimeSetUp()
        # print()
        self.lp = LoginPage(self.driver)


    #
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True