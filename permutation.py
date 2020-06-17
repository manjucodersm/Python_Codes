'''permutation problem'''

from itertools import permutations as perm
def permutations(string):
    perm_list = []
    permutation = perm(string)
    for i in list(permutation):
        k = ''.join(i)
        if not k in perm_list:
            perm_list.append(k)
    return perm_list

if __name__ == '__main__':
    string = 'abcd'
    print permutations(string)
