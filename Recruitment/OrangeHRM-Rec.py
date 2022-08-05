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

class TestRecruitment(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_DeleteRecord(self): #Delete a candidate's record
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@type='checkbox'][1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(1)
        driver.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(1)

        response_message = driver.find_element(By.ID,"frmList_ohrmListComponent").text
        self.assertIn('Deleted', response_message)
   
    

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

