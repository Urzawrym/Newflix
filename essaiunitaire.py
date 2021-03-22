import UnitTest.monProgramme as mp
import unittest

class TestMonProgramme(unittest):

    def testMultiplication(self):

        r = mp.multiplication(2,3)
        self.assertEqual(r,6)

if __name__ == "__main__":
    unittest.main()