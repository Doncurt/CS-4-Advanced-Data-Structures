import unittest
from bit_manipulator_01 import BitManipulation

class test(unittest.TestCase):
    def  testBitManipulation(self):
        a=BitManipulation('00000000','00000001')
        # testing the type to make sure it is of bit manipulation type and can run it's methods
        self.assertTrue(type(a),BitManipulation)
        # testing the add function
        self.assertTrue(a.add(),'0b10')
        # testing the diffrence function
        self.assertTrue(a.differences(),"2")
if __name__ == '__main__':
    unittest.main()
