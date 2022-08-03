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

class TestTime(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_SearchProject(self): #Search a project by a valid customer name
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_time_viewTimeModule").click()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_ProjectInfo")).perform()
        time.sleep(1)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchProject_customer").send_keys("Apache Software Foundation")
        time.sleep(1)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(1)

        response_message = driver.find_element(By.XPATH,"//tbody/tr[1]").text
        self.assertIn('Apache Software Foundation', response_message)
   
    def test_b_SearchProjectFailed(self): #Search a project by an invalid customer name
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_time_viewTimeModule").click()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_ProjectInfo")).perform()
        time.sleep(1)
        driver.find_element(By.ID,"menu_admin_viewProjects").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchProject_customer").send_keys("Facebook")
        time.sleep(1)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(1)

        response_message = driver.find_element(By.XPATH,"//tbody/tr[1]").text
        self.assertIn('No Records Found', response_message)

    
    def tearDown(self):
        self.driver.close()

unittest.main()
