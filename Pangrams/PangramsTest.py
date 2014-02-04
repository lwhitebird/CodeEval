import unittest
import Pangrams

class KnownStringtoOutputs(unittest.TestCase):
    knownValues = ( ('A quick brown fox jumps over the lazy dog', 'NULL'),
                    ('A slow ye fx crals under the proactive dog', 'bjkmqz'),
                    ('abcdefghijklmnopqrstuvwxyz', 'NULL'),
                    ('1234524536 13423 2342', 'abcdefghijklmnopqrstuvwxyz'),
                    ('fools, larks alike.', 'bcdghjmnpqtuvwxyz'),
                    ('', 'abcdefghijklmnopqrstuvwxyz'),
                    ('z x wur qlkf ba', 'cdeghijmnopstvy'),
                    ('DFGH QRST YZ', 'abceijklmnopuvwx') )

    def test_create(self):
        """create should return known pangram complement for known input string."""        
        for string, output in self.knownValues:     
            pangram_complement = Pangrams.PangramComplement(string)
            result = pangram_complement.create()
            self.assertEqual(result, output)

class AlphabetSubsets(unittest.TestCase):
    nonemptyStrings = ('nonempty', 'this is a string 13 24543', 'MORE LETTERS')
    empty = ''
    pangram_complement = Pangrams.PangramComplement('')
    expectedTriples = (('j', 'ajbc', 'abc'), ('f', 'ajbc', 'ajbc'), ('', 'adfjl', 'adfjl'), ('q', '', ''))


    def test_return_subset(self):
        """return_subset_or_null should return any nonempty string input."""
        for string in self.nonemptyStrings:
            self.pangram_complement.alphabet_subset = string
            result = self.pangram_complement.return_subset_or_null()
            self.assertEqual(result, string)
        
    def test_return_null(self):
        """return_subset_or_null should return 'NULL' for any empty string input."""
        self.pangram_complement.alphabet_subset = self.empty
        result = self.pangram_complement.return_subset_or_null()
        self.assertEqual(result, 'NULL')

    def test_remove(self):
        """remove should remove inputs if present in string"""
        for letter, alphabet_subset, expected in self.expectedTriples:
            self.pangram_complement.alphabet_subset = alphabet_subset
            self.pangram_complement.remove(letter)
            result = self.pangram_complement.alphabet_subset
            self.assertEqual(result, expected)

if __name__ ==  "__main__":
    unittest.main()
