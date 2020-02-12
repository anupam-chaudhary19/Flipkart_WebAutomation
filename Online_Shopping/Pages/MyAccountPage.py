from Online_Shopping.Locators.GlobalLocators import Locators


class MyAccountPage():
    def __init__(self, driver):
        self.driver = driver

        # created all login page objects

        self.Phone_textbox = Locators.Enter_Phone
        self.Continue_Btn = Locators.Continue_btn
        self.Create_New = Locators.Create_New

    def click_createnewaccount(self):
        self.driver.find_element_by_xpath(Locators.Create_New).click()



    def enter_phone(self, phone):
        #self.driver.find_element_by_xpath(Locators.password_textbox).clear()
        self.driver.find_element_by_xpath(Locators.Enter_Phone).send_keys(phone)

    def click_continuebtn(self):
        #self.driver.find_element_by_xpath(Locators.password_textbox).clear()
        self.driver.find_element_by_xpath(Locators.Continue_btn).click()