
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os

#from Online_Shopping.Pages.ContactUs import ContactUs

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Online_Shopping.Pages.FlipkartLoginPage import LoginPage
from Online_Shopping.Pages.MyAccountPage import MyAccountPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Anupam/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_Createlogin(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        accountpage = MyAccountPage(driver)
        #login = LoginPage(driver)
        Titleofwebpage = driver.title
        self.assertEqual("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!", Titleofwebpage)
        accountpage.click_createnewaccount()
        accountpage.enter_phone("9872441633")
        accountpage.click_continuebtn()


       # MyAccountpage = MyAccountPage(driver)
       #MyAccountpage.click_orderhistoryanddetails()

        #MyAccountpage.click_signout()
        driver.close()
    def test_02_login_valid(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")

        login = LoginPage(driver)
        Titleofwebpage = driver.title
        self.assertEqual("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!", Titleofwebpage)
        login.enter_email("testerac7212@gmail.com")
        login.enter_password("zxcv@1234")
        login.click_login()

       # MyAccountpage = MyAccountPage(driver)
       #MyAccountpage.click_orderhistoryanddetails()

        #MyAccountpage.click_signout()
        driver.close()
    @classmethod
    def tearDown(cls):
        # cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Anupam/PycharmProjects/Flipkart_WebAutomation/Reports'))
