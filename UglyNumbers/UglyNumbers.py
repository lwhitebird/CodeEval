import sys
test_cases = open(sys.argv[1], 'r')

class OutOfRangeError(Exception): pass


class UglyNumbers:
    def __init__(self):
        self = self.split('')

def is_ugly(number):
    truth = False
    single_digit_primes = [2, 3, 5, 7]
    for prime in single_digit_primes:
        if number % prime == 0:
            truth = True
            break
    return truth

def list_possible_sums(digitstring):
    pass
  

test_cases.close()
