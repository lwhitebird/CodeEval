import unittest
import UglyNumbers

class KnownUglyValues(unittest.TestCase):
    uglys = (0, -6)
    nonUglys = (11, -13, -121, 143, 169)

    def testUgly(self):
        """EvaluateIfUgly should return True for ugly numbers."""
        for ugly in self.uglys:
            result = UglyNumbers.is_ugly(ugly)
            self.assertTrue(result)

    def testNotUgly(self):
        """EvaluateIfUgly should return False for non-uglys."""
        for nonugly in self.nonUglys:
            result = UglyNumbers.is_ugly(nonugly)
            self.assertFalse(result)

class KnownSumValues(unittest.TestCase):
# add more values to test
    knownSumValues = ( (5670, (5670, 8, 18)), (0, (0)) )
    knownNonSumValues = ( (5670, (6, 0, 1)), (0, (1, 2, -3)) )

    def testKnownSumsIncluded(self):
        """All possible sum values should return in sums list."""
        for knownSum in self.knownSumValues:
            digitstring = knownSum[0]
            sums = knownSum[1]
            possible_sums = UglyNumbers.list_possible_sums(digitstring)
            for sum in sums:
                self.assertTrue(sum in possible_sums)

    def testKnownNonSumsNotIncluded(self):
        """No non-sum values should return in sums list."""
        for knownNonSum in self.knownSumValues:
            digitstring = knownNonSum[0]
            sums = knownNonSum[1]
            possible_sums = UglyNumbers.list_possible_sums(digitstring)
            for sum in sums:
                self.assertFalse(sum in possible_sums)

class evaluate_if_ugly_bad_input(unittest.TestCase):
    def testNonInteger(self):
        """evaluate_if_ugly should fail with non-integer type input."""
        self.assertRaises(TypeError, UglyNumbers.is_ugly, '12')

    def testTooLarge(self):
        """evaluate_if_ugly should fail with input over 13 digits."""
        self.assertRaises(UglyNumbers.OutOfRangeError, UglyNumbers.is_ugly, 12345678901234)

class list_possible_sums_bad_input(unittest.TestCase):
    def testNonInteger(self):
        """list_possible_sums should fail with non-integer type input."""
        self.assertRaises(TypeError, UglyNumbers.list_possible_sums, 'hello')

    def testTooLarge(self):
        """evaluate_if_ugly should fail with input over 13 digits."""
        self.assertRaises(UglyNumbers.OutOfRangeError, UglyNumbers.list_possible_sums, 12345678901234)


if __name__ == "__main__":
  unittest.main() 
