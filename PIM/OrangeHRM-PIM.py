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

class TestPIM(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_RunReport(self): #Run a report
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_core_viewDefinedPredefinedReports").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/a[1]").click()
        time.sleep(1)
    

        response_data = driver.find_element(By.ID,"search-results")
        self.assertTrue(response_data)
   
    
    def tearDown(self):
        self.driver.close()

unittest.main()
