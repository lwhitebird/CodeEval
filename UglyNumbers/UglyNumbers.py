import sys, time

start_time = time.time()

class Operators():
    def __init__(self, length):
        self.operatorlist = []
        self.length = length
        for i in range(length):
            self.operatorlist.append('+')
        self.current = length - 1
        self.alphabet = ('+','','+-')

    def create_next_configuration(self):
        operator_list_index = self.current
        if self.current > -1:
            operator = self.operatorlist[operator_list_index]
            alphabet_index = self.alphabet.index(operator)
            next_alph_index = (alphabet_index + 1) % 3
            next_operator = self.alphabet[next_alph_index]
            self.operatorlist[operator_list_index] = next_operator
            if next_operator == '+':
                self.current = operator_list_index - 1
                self.create_next_configuration()

class Sums():
    def __init__(self, digitstring):
        self.generator = digitstring
        self.evaluated_sums_with_count = dict()
        self.combined_current = ''
        self.evaluated_sum = ''

    def evaluate(self):
        separated_sum = self.combined_current.split('+')
        total = 0
        for number in separated_sum:
            total += int(number)
        self.evaluated_sum = total

    def track_count(self):
        total_exists = self.evaluated_sums_with_count.has_key(self.evaluated_sum)
        total = self.evaluated_sum
        if total_exists:
            count_of_total = self.evaluated_sums_with_count.get(total) + 1
            self.evaluated_sums_with_count[total] = count_of_total
        else:
            self.evaluated_sums_with_count[total] = 1
            
    def combine_operators_with_generator(self, operators):
        operators = operators.operatorlist
        generator = self.generator
        combined = generator[0]
        for i in range(len(generator) - 1):
            combined += operators[i]
            combined += generator[i + 1]
        self.combined_current = combined
 
def is_ugly(number):
    isugly = False
    single_digit_primes = [2, 3, 5, 7]
    for prime in single_digit_primes:
        if number % prime == 0:
            isugly = True
            break
    return isugly



test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    strippedtest = test.strip('\n')
    if strippedtest:
        totaluglys = 0
        sums = Sums(strippedtest)
        test_length = len(strippedtest)
        remaining_configurations = pow(3, test_length - 1)
        operators = Operators(test_length - 1)
        while remaining_configurations > 0 :
            sums.combine_operators_with_generator(operators)
            sums.evaluate()
            sums.track_count()
            operators.current = operators.length - 1
            operators.create_next_configuration()
            remaining_configurations -= 1
        for evaluated_sum in sums.evaluated_sums_with_count:
            if is_ugly(evaluated_sum):
                totaluglys += sums.evaluated_sums_with_count[evaluated_sum]
        print totaluglys

test_cases.close()
print str(time.time() - start_time) + " seconds"
