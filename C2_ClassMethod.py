import unittest
class TestCaseDemo(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  print("setUpClass method")

 def setUp(self):	#Not Allowed to change the name
  print("setup method execution, flow checking purpose")

 def test_method1(self):	
  print("test1 running")

 def test_method2(self):
  print("test 2 running")
  print(10/0)

 def test_method3(self):
  print("test 3 running")
  print(10/0)

 def test_method4(self):
  print("test 4 running")

 def tearDown(self):
  print("tearDown method execution, flow checking purpose")

 @classmethod
 def tearDownClass(cls):
  print("tearDownClass method execution")

unittest.main()	#calling, in this file, is there any class which is child of TestCase. In that setup, test, and tearDown() will be executed



