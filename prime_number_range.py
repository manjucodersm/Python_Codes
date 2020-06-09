'''This Program finds the All prime numbers in a given range'''


def primeNumberRange(start, end):
    '''Finds the All prime numbers in a given range
    Input : start and end number
    Output: Print All prime numbers in a given range'''
    print primeNumberRange.__doc__

    for number in range(start, end+1):
        for num in range(2, (number//2)+1):
            if not number%num:
                break
        else:
            if number >= 2:
                print "%d" % number


if __name__ == '__main__':
    start = input("Enter a start range : ")
    end = input("Enter a end range : ")
    primeNumberRange(start, end)
