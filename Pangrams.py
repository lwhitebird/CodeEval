import sys
test_cases = open(sys.argv[1], 'r')

def missing(string):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for letter in string:
    letterlower = letter.lower()
    if letterlower in alphabet: alphabet = alphabet.replace(letterlower, '')
  if alphabet: return alphabet
  else: return 'NULL'
  
for test in test_cases:
  print missing(test)
  
test_cases.close()