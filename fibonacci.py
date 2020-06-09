'''This program finds the Fibonacci series'''

def fibonacci(num):
    '''Finds the Fibonacci series
    Input : num
    Output: Print Fibonacci series'''

    num1 = 0
    num2 = 1
    print "%d\n%d" % (num1, num2)

    for _ in range(num-2):
        num1, num2 = num2, num1+num2
        print "%d" % num2

if __name__ == '__main__':
    num = input("Enter Fibonacci series length")
    fibonacci(num)
