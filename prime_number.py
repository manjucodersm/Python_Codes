'''This Program checks whether a number is prime or not'''


def primeNumber(number):
    '''Checking number is prime or not
    Input : Any number
    Output: Print number is prime or not'''
    print primeNumber.__doc__

    if number == 1 or (number != 2 and number%2 == 0):
        print "\n%d is not a prime number" % number
        return

    for num in range(3, (number//2)+1, 2):
        if not number%num:
            print "\n%d is not a prime number" % number
            break
    else:
        print "\n%d is a prime number" % number


if __name__ == '__main__':
    num = input("Enter a number to check whether it's a prime or not : ")
    primeNumber(num)
