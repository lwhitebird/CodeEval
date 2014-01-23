import unittest
import Pangrams

class KnownValues(unittest.TestCase):
  knownValues = ( ('A quick brown fox jumps over the lazy dog', 'NULL'),
                  ('A slow yellow fox crawls under the proactive dog', 'bjkmqz'))
    
  def testMissing(self):
    """Pangrams should give known result with known input."""
    for string, output in self.knownValues:
      result = Pangrams.missing(string)
      self.assertEqual(result, output)

#This could be testing for anything, regardless of whether known value. Not totally sure how to test for that, yet.
  def testMissingCase(self):
    """Pangrams should return 'NULL' or all lowercase letters."""
    for string, output in self.knownValues:
      result = Pangrams.missing(string)
      if output != 'NULL': self.assertEqual(result, result.lower())

#This could be testing for anything, regardless of whether known value. Not totally sure how to test for that, yet.
  def testMissingOrder(self):
    """Pangrams should always return in alphabetical order."""
    for string, output in self.knownValues:
      result = Pangrams.missing(string)
      resultlist = result.split()
      resultlist.sort()
      sortedresult = ''.join(resultlist)
      self.assertEqual(result, sortedresult)

if __name__ ==  "__main__":
  unittest.main()