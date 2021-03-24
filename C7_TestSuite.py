import unittest
from C7_testcase1 import *
from C7_testcase2 import *
#load all the test case from testcase1 and testcase2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

#create a testsuite
ts = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)
