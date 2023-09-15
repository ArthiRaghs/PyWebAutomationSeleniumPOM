from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
import logging
import pytest
from src.pageObjects.loginPage import *


class TestVwoLogin:


    @pytest.fixture()
    def driver(self):
        driver=webdriver.Chrome()
        driver.get("https://app.vwo.com")
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.mark.positive
    def test_vwologin(self,driver):
        #Logger=logging.Logger(__name__)
        #selenium API create session
        # driver=webdriver.Chrome()
        # driver.maximize_window()
        # driver.get("https://app.vwo.com")
        #driver=setup
        loginPage=LoginPage(driver)
        loginPage.login_to_vwo("contact+augg@thetestingacademy.com","Wingify@123")
        assert "Login - VWO" in driver.title
        time.sleep(5)
