from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variables
username = "Admin"
password = "admin123"
url      = "https://opensource-demo.orangehrmlive.com/"

class TestLeave(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_AssignLeaveBlank(self): #assign leave with blank fields
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_leave_viewLeaveModule").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_leave_assignLeave").click()
        time.sleep(1)
        driver.find_element(By.ID,"assignBtn").click()
        time.sleep(1)
    

        response_data = driver.find_element(By.CLASS_NAME,"validation-error")
        self.assertTrue(response_data)
   
    

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
