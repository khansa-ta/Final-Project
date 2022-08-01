from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variables
username = "Admin"
password = "admin123"
url      = "https://opensource-demo.orangehrmlive.com/"

class TestDashboard(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_VerifyQuickLunch(self): #Verify if a Quick Lunch button directs user to the correct page
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div[1]/a[1]/img[1]").click()
        time.sleep(1)
        
        response_data = driver.find_element(By.ID,"assign-leave").text
        self.assertIn('Assign Leave', response_data)

    def test_b_Chart(self): #Verify if the chart of Employee Distribution is shown
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(5)
        
        response_data = driver.find_element(By.TAG_NAME, "canvas").is_displayed
        self.assertTrue(response_data)
    
    def tearDown(self):
        self.driver.close()

unittest.main()
