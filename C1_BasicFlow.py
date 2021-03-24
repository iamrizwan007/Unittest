import unittest
class TestCaseDemo(unittest.TestCase):
 def setUp(self):	#Not Allowed to change the name
  print("setup method execution, flow checking purpose")

 def test_method1(self):	#Can change, but condition it should be prefixed with test only, ex:test_method(self)
  print("test1 running")
  #print(10/0)		#Failed

 def test_method2(self):
  print("test 2 running")

 def tearDown(self):	#Not Allowed to change the name
  print("tearDown method execution, flow checking purpose")

unittest.main()	#calling, in this file, is there any class which is child of TestCase. In that setup, test, and tearDown() will be executed



