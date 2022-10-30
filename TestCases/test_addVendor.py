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


class Test_012_addVendor:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_addVendor(self):
        self.logger.info("****** Test_012_addVendor ******")
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

        self.logger.info("******* Starting Add Vendor Test *******")
        # To open CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()

        # To open CustomerItem
        self.driver.find_element(By.XPATH,"//a[@href='/Admin/Vendor/List']").click()

        # To add New Vendor

        self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()

        Name=self.driver.find_element(By.XPATH,"//input[@id='Name']")
        Name.send_keys('Vendor3')
        innerframe=self.driver.find_element(By.XPATH,"//iframe[@id='Description_ifr']")
        self.driver.switch_to.frame(innerframe)
        Description=self.driver.find_element(By.XPATH,"//*[@id='tinymce']/p")
        Description.click()
        Description.send_keys("This is New Vendor")
        self.driver.switch_to.parent_frame()

        self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Vendor3@gmail.com")

        self.driver.find_element(By.XPATH,"//button[@name='save']").click()

        self.logger.info("******* Add Vendor Test Passed ******")

        self.logger.info("********* Ending Add Vendor Test ********")


