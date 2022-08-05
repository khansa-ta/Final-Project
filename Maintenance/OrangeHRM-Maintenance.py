from fileinput import filename
from http.client import ImproperConnectionState
from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options

#variables
username = "Admin"
password = "admin123"
url      = "https://opensource-demo.orangehrmlive.com/"

class TestMaintenance(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        
    def test_a_DownloadData(self): #Download data
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_maintenance_purgeEmployee").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_maintenance_accessEmployeeData").click()
        time.sleep(1)
        driver.find_element(By.ID,"confirm_password").send_keys(password)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"div.box:nth-child(1) div.inner form:nth-child(1) div.row div.input-field.col.s12.m12.l4:nth-child(2) > input:nth-child(2)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#employee_empName").send_keys(" ")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body/div[4]/ul[1]/li[1]").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"search_employee").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"div.box:nth-child(1) form:nth-child(2) div.inner div.input-field.col.s12.m12.l4:nth-child(2) > input.search_employee:nth-child(2)").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(1)
        driver.find_element(By.ID,"modal_confirm").click()
        time.sleep(1)
        
        resp = requests.post("https://opensource-demo.orangehrmlive.com/index.php/maintenance/getEmployeeDataApi")
        self.assertEqual(resp.status_code, 200)

        

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
