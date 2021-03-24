import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HMSLoginLogoutDemo(unittest.TestCase):
 
#2 test cases having same browser and website to launch once only, hence class method using
 
 @classmethod
 def setUpClass(cls):
  global driver
  driver = webdriver.Chrome(executable_path='C:\\Users\\mrizwan5\Desktop\\Python\\Selenium\\chromedriver.exe')
  driver.get("http://www.seleniumbymahesh.com/")
  driver.maximize_window()

#TEST:1
 def test_login(self):
  driver.find_element(By.LINK_TEXT,'HMS').click()
  time.sleep(5)
  driver.find_element(By.NAME,'username').send_keys('admin')
  driver.find_element(By.NAME,'password').send_keys('admin')
  driver.find_element(By.NAME,'submit').click()

#TEST:2
 def test_logout(self):
  driver.find_element(By.LINK_TEXT,'Logout').click()
  time.sleep(5)

 @classmethod
 def tearDownClass(cls):
  driver.close()

unittest.main()