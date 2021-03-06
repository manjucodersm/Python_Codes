'''John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper
a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving
and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is
the biggest possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between:
[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and
the distances of the 3 corresponding towns is [55, 58, 60]'''


def chooseBestSum(t, k, ls):
    ls.sort(reverse=True)
    result = None
    for i in range(len(ls)-k+1):
        result_sum = sum(ls[i:i+k])
        if result_sum == t:
            result = result_sum
            break
            
        if result_sum < t:
            count = 0
            store = result_sum
            for j in range(i, 0, -1):
                exp_result = result_sum - ls[j] + ls[j-1]
                if exp_result <= t:
                    count += 1
                    if exp_result > store:
                        store = exp_result

            result = store                            
            break
    
    return result 


if __name__ == '__main__':
    ls = [50, 55, 57, 58, 60]
    if chooseBestSum(174, 3, ls) == 172:
        print 'PASS'
    else:
        print 'FAIL'
