'''This program finds GCD of two numbers'''


def gcd(num1, num2):
    '''Finds the GCD of two numbers
    Input : num1 and num2
    Output: Print GCD of two numbers'''

    if num1 > num2:
        num1, num2 = num2, num1

    while num1:
        num1, num2 = num2%num1, num1

    print "GCD = %d" % num2

if __name__ == '__main__':
    num1 = input("enter 1st number : ")
    num2 = input("enter 2nd number : ")
    gcd(num1, num2)
