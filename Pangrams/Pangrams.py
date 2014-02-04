import sys
test_cases = open(sys.argv[1])

class PangramComplement():
    def __init__(self, string):
        self.alphabet_subset = 'abcdefghijklmnopqrstuvwxyz'
        self.string = string

    def return_subset_or_null(self):
        if self.alphabet_subset:    return self.alphabet_subset
        else:                       return 'NULL'

    def remove(self, letter):
        if letter in self.alphabet_subset:
            self.alphabet_subset = self.alphabet_subset.replace(letter, '')

    def create(self):
        for letter in self.string:
            lowercase_letter = letter.lower()
            self.remove(lowercase_letter)
        return self.return_subset_or_null()

for test in test_cases:
    alphabet_complement = PangramComplement(test)
    print alphabet_complement.create()

test_cases.close()
