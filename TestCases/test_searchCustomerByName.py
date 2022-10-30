import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import string
import random
import time


class Test_005_searchCustomerByName:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_searchCustomerByName(self):
        self.logger.info("****** Test_003_searchCustomerByName ******")
        # To Open Browser
        self.serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
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

        self.logger.info("******* Starting Search Customer By Name Test *******")
        # To open CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()
        # To open the Customer Item from CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a").click()

        # Searching Customer By
        self.driver.find_element(By.XPATH, "//*[@id='SearchFirstName']").click()
        self.driver.find_element(By.XPATH, "//*[@id='SearchFirstName']").send_keys("Victoria")
        self.driver.find_element(By.XPATH, "//input[@id='SearchLastName']").click()
        self.driver.find_element(By.XPATH, "//input[@id='SearchLastName']").send_keys("Terces")
        self.driver.find_element(By.XPATH, "//*[@id='search-customers']").click()
        rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']")
        print(len(rows))
        for r in range(1,len(rows)):
            Name=self.driver.find_elements(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Name == "Victria Terces":

                print("Test Passed")
                self.driver.close()
                self.logger.info("******* Search Customer By Name Test Passed *******")

            else:
                print("Test Failed")
                self.driver.close()
                self.logger.error("****** Search Customer By Name Test Failed ******")


        self.logger.info("******** Test Case Search Customer By Name id finished ********")



