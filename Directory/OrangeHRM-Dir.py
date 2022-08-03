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

class TestDirectory(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_SearchNameInvalid(self): #Search an invalid name
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("Jessica")
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)

        response_message = driver.find_element(By.XPATH,"//body/div[@id='wrapper']/div[@id='content']/div[2]/div[2]").text
        self.assertIn('No Records Found', response_message)


    
    def tearDown(self):
        self.driver.close()

unittest.main()
