import sys
test_cases = open(sys.argv[1])

def return_string_or_null(string):
    if string:  return string
    else:       return 'NULL'

def remove_if_present(letter, alphabet_subset):
    if letter in alphabet_subset:
        return alphabet_subset.replace(letter, '')
    else: return alphabet_subset

def needed_for_pangram(string):
    alphabet_subset = 'abcdefghijklmnopqrstuvwxyz'
    for letter in string:
        lowercase_letter = letter.lower()
        alphabet_subset = remove_if_present(lowercase_letter, alphabet_subset)
    return return_string_or_null(alphabet_subset)

for test in test_cases:
    letters_needed_to_be_pangram(test)

test_cases.close()
