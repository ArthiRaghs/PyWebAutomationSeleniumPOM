#Page locators
#Page actions
# Webdriver -  init
# Custom functions
# Page classes
from selenium.webdriver.common.by import By
from tests.vwoLogin.test_vwologin import *

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

    #Page locators
    username=(By.ID,"login-username")
    password=(By.NAME,"password")
    submit_button=(By.XPATH,"//button[@id='js-login-btn']")
    error_message=(By.CSS_SELECTOR,"#js-notification-box-msg")

    #Page actions- return a web element
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)
    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)
    def login_to_vwo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

