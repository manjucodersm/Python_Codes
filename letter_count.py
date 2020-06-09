'''This program finds letters count'''


def letterCount(string):
    '''Finds the number of letters repeated in a string
    Input : string
    Output: Print number of repeated letters in dictionary'''
    print letterCount.__doc__

    dic = {}
    for latter in string:
        if latter in dic:
            dic[latter] += 1
        else:
            dic[latter] = 1
    print dic


if __name__ == '__main__':
    string = raw_input("Enter a string : ")
    letterCount(string)

