'''Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples: Testing: [0, 0, 0, 1] ==> 1, Testing: [0, 0, 1, 0] ==> 2 etc...'''


def binaryArrayToNumber(arr):
  bin_ch = ''
  for i in arr:
      bin_ch += str(i)
  
  return int(bin_ch, 2)

if __name__ == '__main__':
    arr = [0, 1, 0, 1]
    print binaryArrayToNumber(arr)
