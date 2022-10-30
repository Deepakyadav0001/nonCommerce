import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import Select
from utilities import XLUtils
import string
import random
import time


class Test_007_deleteCustomer:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_deleteCustomer(self):
        self.logger.info("****** Test_007_deleteCustomer ******")
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

        self.logger.info("******* Starting Delete Customer Test *******")
        # To open CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()
        # To open the Customer Item from CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a").click()

        # editing Customer Details

        # To get the customer info
        self.driver.find_element(By.XPATH, "//*[@id='SearchEmail']").click()
        self.driver.find_element(By.XPATH, "//*[@id='SearchEmail']").send_keys("victoria_victoria@nopCommerce.com")
        self.driver.find_element(By.XPATH, "//*[@id='search-customers']").click()
        time.sleep(3)

        # To open customer details
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-default']").click()

        # To delete a Customer
        self.driver.find_element(By.XPATH,"//span[@id='customer-delete']").click()
        self.driver.close()

        self.logger.info("******** Customer Successfully Deleted *********")

        self.logger.info("******** Ending Delete Customer Test ********")