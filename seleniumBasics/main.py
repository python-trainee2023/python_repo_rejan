from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseClass:
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")

    def teardown(self):
        self.driver.close()


class SauceDemo(BaseClass):
    def __init__(self):
        super().__init__()
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.loginBtn = (By.ID, "login-button")

    def login(self, username, password):
        self.clearInput(self.username)
        self.inputText(self.username, username)
        self.clearInput(self.password)
        self.inputText(self.password, password)
        self.driver.find_element(*self.loginBtn).click()  # Unpack the tuple with *

    def clearInputs(self):
        self.clearInput(self.username)
        self.clearInput(self.password)

    def clearInput(self, locator):
        self.driver.find_element(*locator).clear()

    def inputText(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)


# Instantiate the SauceDemo class
loginDemo = SauceDemo()

try:
    loginDemo.setup()
    loginDemo.login("standard_user", "secret_sauce")
except Exception as e:
    print(e)
finally:
    sleep(5)
    loginDemo.teardown()
