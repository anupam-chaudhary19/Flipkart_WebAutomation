from Online_Shopping.Locators.GlobalLocators import Locators
import HTMLReport


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        # created all login page objects

        self.EnterEmail_textbox = Locators.Email_textbox
        self.password_textbox = Locators.password_textbox
        self.Login_button = Locators.Login_button

    def enter_email(self, email):
        self.driver.find_element_by_xpath(Locators.Email_textbox).clear()
        self.driver.find_element_by_xpath(Locators.Email_textbox).send_keys(email)


    def enter_password(self, password):
        self.driver.find_element_by_xpath(Locators.password_textbox).clear()
        self.driver.find_element_by_xpath(Locators.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.Login_button).click()


