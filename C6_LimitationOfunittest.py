import unittest
class TestCaseDemo(unittest.TestCase):
 def test_C(self):
  print("test C execution...")

 def test_B(self):
  print("test B execution...")

 def test_A(self):
  print("test A execution...")

class TestCaseDemo2(unittest.TestCase):
 def test_D(self):
  print("test D execution...")

 def test_E(self):
  print("test E execution...")

 def test_F(self):
  print("test F execution...")

unittest.main()