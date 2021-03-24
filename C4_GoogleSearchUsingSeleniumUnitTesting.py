from selenium import webdriver
import unittest
import time
class GoogleSearchDemo(unittest.TestCase):
 def setUp(self):
  global driver
  driver = webdriver.Chrome(executable_path='C:\\Users\\mrizwan5\Desktop\\Python\\Selenium\\chromedriver.exe')
  driver.get("https://www.google.com/")
  driver.maximize_window()

 def test_google_srch(self):
  print('test method execution')
  driver.find_element_by_name('q').send_keys('Mahesh Babu')
  time.sleep(5)
  driver.find_element_by_name('btnK').click()
  time.sleep(2)
  driver.find_element_by_class_name('LC20lb').click()
  title = driver.title
  if title == 'Mahesh Babu - Wikipedia':
   print("Correct page title",title)
  else:
   print("incorrect title, got:",title)
  time.sleep(2)
 
 def tearDown(self):
  driver.close()
  
unittest.main()
  