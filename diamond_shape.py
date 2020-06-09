'''This program print in diamond shape with any symbol'''

def diamondShape(num, ch):
    '''Print diamond shape with any symbol
    Input : num and ch (symbol)
    Output: Print diamond shape with any symbol'''
    print diamondShape.__doc__

    for i in range(1, num+1, 2):
        print (ch*i).center(num, ' ')

    for j in range(num-2, 0, -2):
        print (ch*j).center(num, ' ')


if __name__ == '__main__':
    num = input("Enter width of diamond shape : ")
    ch = raw_input("Enter fill character in diamond shape : ")
    diamondShape(num, ch)
