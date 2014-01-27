import sys
test_cases = open(sys.argv[1], 'r')

class OutOfRangeError(Exception): pass

def is_ugly(number):
    isugly = False
    single_digit_primes = [2, 3, 5, 7]
    for prime in single_digit_primes:
        if number % prime == 0:
            isugly = True
            break
    return isugly

def triplepossums(possums, index):
    possumsplaceholder = list(possums)
    for possum in possums:
        newindex = len(possum) - index
        summed = possum[:newindex] + '+' + possum[newindex:]
        minused = possum[:newindex] + '+-' + possum[newindex:]
        possumsplaceholder.append(summed)
        possumsplaceholder.append(minused)
    return possumsplaceholder

def nueval(possum):
    separatedpossum = possum.split('+')
    tsum = 0
    for sep in separatedpossum:
        tsum += int(sep)
    return tsum

def evalpossums(possums):
    possumplaceholder = list(possums)
    for possum in possums:
        possumindex = possums.index(possum)
        possumplaceholder[possumindex] = nueval(possum)
    return possumplaceholder

def list_possible_sums(digitstring):
    possible_sums = list()
    possible_sums.append(digitstring)
    for i in reversed(range(1, len(digitstring))):
        possible_sums = triplepossums(possible_sums, i)
    return evalpossums(possible_sums)

for test in test_cases:
    strippedtest = test.strip('\n')
    if strippedtest:
        totaluglys = 0
        possums = list_possible_sums(strippedtest)
        for possum in possums:
            if is_ugly(possum): totaluglys += 1
        print totaluglys

test_cases.close()
