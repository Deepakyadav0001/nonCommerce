import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities.readproperties import Readconfig
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_Login_DDT:
    baseUrl = Readconfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()


    def test_Login_ddt(self):
        self.logger.info("****** Test_002_Login_DDT ******")
        self.logger.info("****** Verifying Login Test ******")
        self.serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get(self.baseUrl)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

        self.driver.find_element(By.XPATH, "//*[@id='Email']").click()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='Email']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//input[@id='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

        act_title=self.driver.title
        exp_title="Dashboard / nopCommerce administration"

        if act_title==exp_title:
            if self.exp=='Pass':
                self.logger.info("**** passed ****")
                self.LoginPage.clickLogout();
                lst_status.append("Pass")
            elif self.exp=='Fail':
                self.logger.info("**** failed ****")
                self.LoginPage.clickLogout();
                lst_status.append("Fail")

        elif act_title!=exp_title:
            if self.exp == 'Pass':
                self.logger.info("**** failed ****")
                lst_status.append("Fail")
            elif self.exp == 'Fail':
                self.logger.info("**** passed ****")
                lst_status.append("Pass")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");
