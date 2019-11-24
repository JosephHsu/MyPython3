import unittest
import calc

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3,2)

    def tearDown(self):
        self.args = None

#shortcut : move a line up => alt upArrow ; delete a line => ctrl +x
# 方法的開頭必須為test
    def test_plus(self):
        expected = 5
        result = calc.plus(*self.args)
        self.assertEqual(expected,result)

    def test_helloWorld(self):
        self.assertEqual(calc.helloWorld(),'hello~world')

if __name__ == '__main__':
    unittest.main()