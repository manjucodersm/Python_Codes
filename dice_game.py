'''Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450'''


def score(dice):
    dic = {'111': 1000, '222': 200, '333':300, '444':400,
           '555':500, '666': 600, '1':100, '5':50}
    dice.sort()
    st = ''
    for i in dice:
        st += str(i)
    result = 0
    for j in dic:
        while j in st:
            result += dic[j]
            st = st[:st.find(j)]+st[st.find(j)+len(j):]
    
    return result


if __name__ == '__main__':
    dice = [5, 1, 3, 4, 1]
    if score(dice) == 250:
        print 'PASS'
    else:
        print 'FAIL'
