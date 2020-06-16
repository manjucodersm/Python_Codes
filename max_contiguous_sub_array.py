'''The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) ==> should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum
is the sum of the whole array. If the list is made up of only negative numbers,
return 0 instead. Empty list is considered to have zero greatest sum.

Note that the empty list or array is also a valid sublist/subarray'''


def maxSequence(arr):
    max_seq_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr_sum = 0
            for k in range(j, len(arr)):
                arr_sum += arr[k]        
                if arr_sum > max_seq_sum:
                    max_seq_sum = arr_sum
                
    return max_seq_sum


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    if maxSequence(arr) == 6:
        print 'PASS'
    else:
        print 'FAIL'
