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

class TestPerformance(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_ChangeAchievement(self): #Edit a log by changing Achievement
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu__Performance")).perform()
        time.sleep(1)
        driver.find_element(By.ID,"menu_performance_viewEmployeePerformanceTrackerList").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"div.box:nth-child(1) div.inner table.table.hover tbody:nth-child(2) tr.odd:nth-child(1) td.left:nth-child(1) > a:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"div.box:nth-child(3) div.inner table.table.hover tbody:nth-child(2) tr.odd td.left:nth-child(1) > a:nth-child(1)").click()
        time.sleep(1)
        elem1 = driver.find_element(By.XPATH,"//option[contains(text(),'Positive')]")
        elem2 = driver.find_element(By.XPATH,"//option[contains(text(),'Negative')]")
        if elem1.is_selected():
            driver.find_element(By.ID,"addperformanceTrackerLog_achievement").click()
            elem2.click()
        else:
            elem1.click()
        time.sleep(1)
        driver.find_element(By.ID,"saveBtn").click()
        time.sleep(1)


        response_message = driver.find_element(By.ID,"search-results").text
        self.assertIn("Saved", response_message)
   
    

    
    def tearDown(self):
        self.driver.close()

unittest.main()
