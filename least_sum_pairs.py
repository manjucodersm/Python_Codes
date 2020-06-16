'''Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10'''


def sumPairs(ints, s):
    result = None
    min_index = len(ints)
    for i in range(len(ints)-1):
        for j in range(i+1, len(ints)):
            if (ints[i] + ints[j] == s) and (min_index > j):
                result = [ints[i], ints[j]]
                min_index = j
    return result

if __name__ == '__main__':
    ints = [11, 3, 7, 5]
    if sumPairs(ints, 10) == [3, 7]:
        print "PASS"
    else:
        print 'FAIL'
