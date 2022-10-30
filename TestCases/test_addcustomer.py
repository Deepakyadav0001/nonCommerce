import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from PageObjects.LoginPage import LoginPage
import string
import random

class Test_003_AddCustomer:
    baseUrl=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_addCustomer(self):
        self.logger.info("****** Test_003_AddCustomer ******")
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

        self.logger.info("******* Starting Add Customer Test *******")
        # To open CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()
        # To open the Customer Item from CustomerMenu
        self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a").click()
        # To Add New Customer
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()

        # ***** Adding all Customer details *****

        # 1. To Add Email
        Email= random_generator() + "@gmail.com"
        Emailaddress=self.driver.find_element(By.XPATH,"//input[@id='Email']")
        Emailaddress.click()
        Emailaddress.send_keys(Email)

        # 2. To Add Password
        Password=self.driver.find_element(By.XPATH,"//input[@id='Password']")
        Password.click()
        Password.send_keys("testing")

        # 3.To Add First Name
        FirstName=self.driver.find_element(By.XPATH,"//input[@id='FirstName']")
        FirstName.click()
        FirstName.send_keys("Deepak")

        # 4. To Add Last Name
        LastName=self.driver.find_element(By.XPATH,"//input[@id='LastName']")
        LastName.click()
        LastName.send_keys("Yadav")

        # 5. To Select Male Gender
        self.driver.find_element(By.XPATH,"//input[@id='Gender_Male']").click()

        # 6. To Enter DOB
        DOB=self.driver.find_element(By.XPATH,"//input[@id='DateOfBirth']")
        DOB.click()
        DOB.send_keys("18/01/2002")

        # 7. To Enter the Company Name
        CompanyName=self.driver.find_element(By.XPATH,"//input[@id='Company']")
        CompanyName.click()
        CompanyName.send_keys("AiDash")

        # 8. To Enter Newsletter
        Newsltr=self.driver.find_elements(By.XPATH,"//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div")
        for nws in Newsltr:
            if nws.text=="Test store 2":
                nws.click()

        # 9. To Select CustomerRoles
        CustomerRoles=self.driver.find_elements(By.XPATH,"//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div")
        for CustRole in CustomerRoles:
            if CustRole.text=="Registered":
                CustRole.click()

        # 10. To Select Manager of Vendor
        Select(self.driver.find_elements(By.XPATH,"//*[@id=VendorId]")).select.by.visible.text("Vendor 1")

        # 11. To Save New Customer
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/div[1]/div/button[1]").click()

        # 12. Admin Comment
        comment=self.driver.find_element(By.XPATH,"//textarea[@id='AdminComment']")
        comment.send_keys("This is Testing...")

        self.logger.info("******* Saving customer info *******")

        self.logger.info("****** Add customer validation started ******")

        self.msg= self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True
            self.logger.info("******* Add Customer Test Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("****** Add customer test failed ******")
            assert False

        self.driver.close()
        self.logger.info("****** Ending Add customer test *******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))








