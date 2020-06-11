'''You are given an array strarr of strings and an integer k.
Your task is to return the first longest string consisting of k
consecutive strings taken in the array.

Example:
strarr = ["zone", "abigail", "theta", "form", "libe",
          "zas", "theta", "abigail"]
k = 2 ==> "abigailtheta"'''


def longestConsecative(strarr, k):
    longest_ch = ''
    for i in range(len(strarr)-k+1):
        ch = ''
        for j in range(k):
            ch += strarr[i+j]
        
        if len(longest_ch) < len(ch):
            longest_ch = ch
    
    return longest_ch


if __name__ == '__main__':
    strarr = ["zone", "abigail", "theta", "form", "libe",
              "zas", "theta", "abigail"]
    print longestConsecative(strarr, 2)
