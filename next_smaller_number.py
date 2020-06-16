'''Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits. For example:

513 ==> 351
2017 ==> 1702'''


from itertools import permutations
def nextSmaller(n):
    n_string = list(str(n))
    result = -1
    for i in range(len(n_string)-1, 0, -1):
        if int(n_string[i]) < int(n_string[i-1]):
            k = ''.join(n_string[i-1:])
            l = []
            for j in permutations(k):
                k1 = int(''.join(j))
                if not k1 in l:
                    l.append(k1)
            l.sort(reverse=True)
            k2 = l[l.index(int(k))+1]
            return int(''.join(n_string[:i-1]) + str(k2))
    else:
        return result


if __name__ == '__main__':
    if nextSmaller(513) == 351:
        print 'PASS'
    else:
        print 'FAIL'
