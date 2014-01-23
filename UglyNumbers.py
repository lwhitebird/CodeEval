import sys
test_cases = open(sys.argv[1], 'r')

def evaluate_if_ugly(number):
  truth = False
  single_digit_primes = [2, 3, 5, 7]
  for prime in single_digit_primes:
    if number % prime == 0:
      truth = True
      break
  return truth

def create_list_possible_sums():
  pass

test_cases.close()
