'''Write a program that will calculate the number of trailing zeros in a factorial of a given number.
N! = 1  2  3  ...  N, Be careful 1000! has 2568 digits...

Examples
zeros(6) = 1
# 6! = 1  2  3  4  5 * 6 = 720 --> 1 trailing zero'''


def factorialTrialZeros(num):
    result = 0
    while num >= 5:
        num = num/5
        result += num
    return result


if __name__ == '__main__':
    if factorialTrialZeros(340) == 83:
        print 'PASS'
    else:
        print 'FAIL'
        
