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


class Test_006_updateCustomerDetails:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_updateCustomerDetails(self):
        self.logger.info("****** Test_006_updateCustomerDetails ******")
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

        self.logger.info("******* Starting Update Customer Details Test *******")
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

        # Updating Customer details

        # 1. changing password
        self.driver.find_element(By.XPATH,"//input[@id='Password']").click()
        self.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("nopCommerce")
        self.driver.find_element(By.XPATH,"//button[@name='changepassword']").click()

        # 5. To Select Female Gender
        self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()

        # 6. To Enter DOB
        DOB = self.driver.find_element(By.XPATH, "//input[@id='DateOfBirth']")
        DOB.click()
        DOB.send_keys("1/8/2020")

        # 7. To Enter the Company Name
        CompanyName = self.driver.find_element(By.XPATH, "//input[@id='Company']")
        CompanyName.click()
        CompanyName.send_keys("AiDash")

        # 8. To Enter Newsletter
        Newsletter = self.driver.find_elements(By.XPATH,"//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div")
        for Nwsltr in Newsletter:
            if Nwsltr.text=='Test store 2':
                Nwsltr.click()
                break

        # 9. To Select CustomerRoles
        CustomerRoles = self.driver.find_elements(By.XPATH,"//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div")
        for CustRole in CustomerRoles:
            if CustRole.text == 'Vendors':
                CustRole.click()
                break


        # 10. To Select Manager of Vendor
        drpdwn=Select(self.driver.find_element(By.XPATH,"//select[@id='VendorId']"))
        drpdwn.select_by_visible_text("Vendor 1")


        # 11. Admin Comment
        comment = self.driver.find_element(By.XPATH, "//textarea[@id='AdminComment']")
        comment.send_keys("This is Testing...")

        # 12. Saving details

        self.driver.find_element(By.XPATH,"//button[@name='save']").click()

        self.driver.close()

        self.logger.info("******** Customer Successfully Updated *********")
        self.logger.info("******* Ending Update Customer Detail Test ********")




