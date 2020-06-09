'''This Program finds LCM of two numbers'''


def lcm(number1, number2):
    '''Finding LCM of two numbers
    Input : num1 and num2
    Output: Print LCM of two numbers'''
    print lcm.__doc__

    num1 = number1
    num2 = number2
    while num1 != num2:
        if num1 < num2:
            num1 += number1
        else:
            num2 += number2
    
    print "LCM of %d and %d is %d" % (number1, number2, num1)


if __name__ == '__main__':
    number1 = input("Enter 1st number : ")
    number2 = input("Enter 2nd number : ")
    lcm(number1, number2)
