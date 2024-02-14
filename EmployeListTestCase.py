# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class EmployeListTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_employe_list_test_case(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("jean")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div[2]/div/div/input").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div[2]/div/div/input").clear()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div[2]/div/div/input").send_keys("Junior Oliveira M Magalhoes")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[6]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[7]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        driver.find_element_by_name("firstName").click()
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("jean")
        driver.find_element_by_name("middleName").click()
        driver.find_element_by_name("middleName").clear()
        driver.find_element_by_name("middleName").send_keys("LILOU")
        driver.find_element_by_name("lastName").click()
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("Jeanne")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/171")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
