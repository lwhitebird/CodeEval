import unittest
import UglyNumbers
# Currently does not test for invalid inputs.

class KnownUglyValues(unittest.TestCase):
  knownUglyValues = ( (0, True), (-6, True), (13, False), (143, False) )
# add more known values to this

  def testEvaluateIfUgly(self):
    """EvaluateIfUgly should return True for ugly numbers and False otherwise."""
    for input, output in self.knownUglyValues:
      result = UglyNumbers.evaluate_if_ugly(input)
      self.assertEqual(result, output)

class KnownSumValues(unittest.TestCase):
# add more known values to this
  knownSumValues = ( (5670, 5670, 8, 18, 6, 0, 1), (0, 0, 0, 0, 1, 2, 3) )

  def testCreateListPossibleSums(self):
    """All possible sum values should return in sums list."""
 # check for validity of using outputs[] here. Probably no.
    for outputs in knownSumValues:
      input = outputs[0]
      list_possible_sums = UglyNumbers.create_list_possible_sums(input)
      for output in outputs[1:4]:
        self.assertTrue(output in list_possible_sums)
      for output in outputs[4:]:
        self.assertFalse(output in list_possible_sums)


if __name__ == "__main__":
  unittest.main() 
