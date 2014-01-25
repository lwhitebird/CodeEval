import unittest
import Pangrams

class KnownValues(unittest.TestCase):
    knownValues = ( ('A quick brown fox jumps over the lazy dog', 'NULL'),
                    ('A slow ye fx crals under the proactive dog', 'bjkmqz'),
                    ('abcdefghijklmnopqrstuvwxyz', 'NULL'),
                    ('1234524536 13423 2342', 'abcdefghijklmnopqrstuvwxyz'),
                    ('fools, larks alike.', 'bcdghjmnpqtuvwxyz'),
                    ('', 'abcdefghijklmnopqrstuvwxyz')  )

    def test_needed_for_pangram(self):
        """needed_for_pangram should give known result for known input."""
        for string, output in self.knownValues:
            result = Pangrams.needed_for_pangram(string)
            self.assertEqual(result, output)

    def test_needed_for_pangram_case(self):
        """needed_for_pangram's return should be all lowercase."""
        upper_partial_alphabet = 'DFGH QRST YZ'
        output = 'abceijklmnopuvwx'
        result = Pangrams.needed_for_pangram(upper_partial_alphabet)
        self.assertEqual(result, output)

    def test_needed_for_pangram_order(self):
        """needed_for_pangram's return should be alphabetized."""
        reverse_partial_alphabet = 'z x wur qlkf ba'
        output = 'cdeghijmnopstvy'
        result = Pangrams.needed_for_pangram(reverse_partial_alphabet)
        self.assertEqual(result, output)

    def test_return_string(self):
        """return_string_or_null should return any nonempty string it is 
        passed."""
        strings = ('nonempty', 'this is a string 13 24543', 'MORE LETTERS')
        for string in strings:
            result = Pangrams.return_string_or_null(string)
            self.assertEqual(result, string)
        
    def test_return_null(self):
        """return_string_or_null should return 'NULL' for any empty string it
        is passed."""
        empty = ''
        result = Pangrams.return_string_or_null(empty)
        self.assertEqual(result, 'NULL')
    
    def test_remove_if_present(self):
        """remove_if_present should remove inputs if present in string, and do
        nothing otherwise"""
        #add error if recieves more than one letter
        expectedTriples = (('j', 'ajbc', 'abc'), ('f', 'ajbc', 'ajbc'), ('', 'adfjl', 'adfjl'), ('q', '', ''))
        for triple in expectedTriples:
            letter = triple[0]
            string = triple[1]
            expected = triple[2]
            result = Pangrams.remove_if_present(letter, string)
            self.assertEqual(result, expected)

if __name__ ==  "__main__":
    unittest.main()

