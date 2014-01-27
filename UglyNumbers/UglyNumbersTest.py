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
# add more values to test, output must be integer
    knownSumValues = ( ('5670', (5670, 567, 567, 675, 72, 72, -665, -62, -62, 126, 63, 63, -14, 49, 49, 81, 18, 18, -59, 4, 4, 69, 6, 6, -71, -8, -8)), ('0', (0,)) )
    knownNonSumValues = ( ('5670', (7, 0, 1)), ('0', (1, 2, -3)) )

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
        for knownNonSum in self.knownNonSumValues:
            digitstring = knownNonSum[0]
            sums = knownNonSum[1]
            possible_sums = UglyNumbers.list_possible_sums(digitstring)
            for sum in sums:
                self.assertFalse(sum in possible_sums)
#may not be necessary
    def testSumIsInteger(self):
        for knownNonSum in self.knownSumValues:
            digitstring = knownNonSum[0]
            possible_sums = UglyNumbers.list_possible_sums(digitstring)
            for sum in possible_sums:
                self.assertTrue(type(sum) == int)
#clunkily added tests, need to be broken out into new classes
    def test_evalpossums(self):
        self.assertEqual(UglyNumbers.evalpossums(('1+2', '3+-4', '1')), [3, -1, 1])

    def test_triplepossums(self):
        print UglyNumbers.triplepossums(('123',), 1)
        self.assertEqual(UglyNumbers.triplepossums(('12',), 1), ['12','1+2','1+-2'])
        self.assertEqual(UglyNumbers.triplepossums(('123',), 1), ['123','12+3','12+-3'])
        self.assertEqual(UglyNumbers.triplepossums(('1+23',), 1), ['1+23','1+2+3','1+2+-3'])

    def testnueval(self):
        self.assertEqual(UglyNumbers.nueval('1+2+3'), 6)
        self.assertEqual(UglyNumbers.nueval('1+-2+3'), 2)
        self.assertEqual(UglyNumbers.nueval('-1+2+3'), 4)
        self.assertEqual(UglyNumbers.nueval('1+-0+3'), 4)

class evaluate_if_ugly_bad_input(unittest.TestCase):
    def testNonInteger(self):
        """evaluate_if_ugly should fail with non-integer type input."""
        self.assertRaises(TypeError, UglyNumbers.is_ugly, '12')

    def testTooLarge(self):
        """evaluate_if_ugly should fail with input over 13 digits."""
        self.assertRaises(UglyNumbers.OutOfRangeError, UglyNumbers.is_ugly, 12345678901234)

#might remove these altogether, may not be necessary
class list_possible_sums_bad_input(unittest.TestCase):
    def testNonInteger(self):
        """list_possible_sums should fail with non-integer type input."""
        self.assertRaises(TypeError, UglyNumbers.list_possible_sums, 'hello')

    def testTooLarge(self):
        """evaluate_if_ugly should fail with input over 13 digits."""
        self.assertRaises(UglyNumbers.OutOfRangeError, UglyNumbers.list_possible_sums, '12345678901234')


if __name__ == "__main__":
  unittest.main() 
