'''This file checks whether a number is prime or not'''


def primeNumber(number):
    '''Checking number is prime or not
    Input : Any number
    Output: True/False'''
    print primeNumber.__doc__
    
    for num in range(2, number//2):
        if not number%num:
            print "\n%d is not a prime number" % number
            break
    else:
        print "\n%d is a prime number" % number


if __name__ == '__main__':
    num = input("Enter a number to check whether it's a prime or not : ")
    primeNumber(num)
