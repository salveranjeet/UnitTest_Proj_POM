from selenium import webdriver
import unittest
import HtmlTestRunner
import time
from PageObjects.LoginPage import LoginPage

import sys
sys.path.append("E:\\python_code\\UnitTest_Proj_POM_Based") ###adding path to path variable in enironment. so that we can run this project through command prompt

class LoginTest(unittest.TestCase):

    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32\\chromedriver.exe')

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.url)
        time.sleep(5)
        cls.driver.maximize_window()

    def test_Login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPasswrod(self.password)
        time.sleep(5)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("OrangeHRM",self.driver.title,"Web page title not matching")
        lp.clickLogout()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output ="E:\\python_code\\UnitTest_Proj_POM_Based\\reports" ))

