import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from utilities import XLUtils
import string
import random
import time


class Test_015_deleteVendor:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_deleteVendor(self):
        self.logger.info("****** Test_015_deleteVendor ******")
        # To Open Browser
        self.serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.implicitly_wait(10)
        # To get to url of website which is being used
        self.driver.get(self.baseUrl)
        # To enter the Email address
        self.driver.find_element(By.XPATH, "//*[@id='Email']").click()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").send_keys(self.username)
        # To Enter the password
        self.driver.find_element(By.XPATH, "//input[@id='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(self.password)
        # To click on the login button
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

        self.logger.info("****** Login Successful *******")

        self.logger.info("******* Starting Delete Vendor Test *******")
        # To open CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()

        # To open CustomerItem
        self.driver.find_element(By.XPATH,"//a[@href='/Admin/Vendor/List']").click()

        # To Search Vendor By Email
        self.driver.find_element(By.XPATH,"//input[@id='SearchEmail']").send_keys("vendor2email@gmail.com")

        self.driver.find_element(By.XPATH, "//button[@id='search-vendors']").click()

        # Deleting Vendor

        self.driver.find_element(By.XPATH,"//a[@class='btn btn-default']").click()

        self.driver.find_element(By.XPATH,"//span[@id='vendor-delete']").click()

        self.driver.find_element(By.XPATH,"//button[normalize-space()='Delete']").click()

        self.logger.info("******** Delete Vendor Test Passed *******")

        self.logger.info("******** Ending Delete Vendor Test ********")

