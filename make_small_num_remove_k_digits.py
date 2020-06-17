'''make small number to remove k digits
#num = "143729" #k:1 => 13729, k:2 => 1329, k:3 => 129, k:4 => 12, k:5 => 1'''


def makeSmallNumRemovekDigits(str_num, k):
    count = i = 0

    while count < k:               
        if int(str_num[i]) > int(str_num[i+1]):
            str_num = str_num[:i] + str_num[i+1:]
            count += 1
            i = 0
        else:
            i += 1
            if len(str_num) == i+1:
                str_num = str_num[:-1]
                count += 1
                i = 0
    return str_num


if __name__ == '__main__':
    str_num = "143729"
    if makeSmallNumRemovekDigits(str_num, 3) == "129":
        print "PASS"
    else:
        print "FAIL"
