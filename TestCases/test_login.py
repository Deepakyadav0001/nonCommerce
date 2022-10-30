import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities.readproperties import Readconfig
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self):

        self.logger.info("******** Test_001_Login ******** ")
        self.logger.info("****** Verifying Homepage Title *******")
        self.serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** Homepage Title Test Passed ******")
        else:
            self.logger.error("****** Homepage Title Test Failed *****")
            self.driver.close()
            assert False


    def test_Login(self):
        self.logger.info("****** Verifying Login Test ******")
        self.serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get(self.baseUrl)
        self.driver.find_element(By.XPATH, "//*[@id='Email']").click()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").send_keys(self.username)
        self.driver.find_element(By.XPATH, "//input[@id='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****** Login Test Passed ******")
            self.driver.close()
        else:
            self.logger.error("****** Login Test Failed ******")
            self.driver.close()
            assert False
