from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage():

    ### identified elements
    username_id = 'txtUsername'
    password_id = 'txtPassword'
    Login_button_id = "btnLogin"
    welcome_id = "welcome"
    logout_linktext = "Logout"

    # driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'

    ### actions need to be performed
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)


    def setPasswrod(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.Login_button_id).click()

    def clickLogout(self):
    #     welcome = self.driver.find_element_by_id("welcome")
    #     logout = self.driver.find_element_by_linkText("Logout")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id(self.welcome_id)).click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text(self.logout_linktext)).click().perform()
