'''Your task is to sort a given string. Each word in the string will contain
a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

Examples
""  -->  ""
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
Note : ' '.join(sorted(sentence.split(), key=min))
'''


def order(sentence):
  if not sentence:
      return ""
      
  result = []
  sub_strings = sentence.split()
  for i in range(1, len(sub_strings)+1):
      for ch in sub_strings:
          if str(i) in ch:
              result.append(ch)
              break
                                            
  return ' '.join(result)


if __name__ == '__main__':
    sentence = raw_input("Enter a sentence")
    expected_result = raw_input("Enter expected result")
    if order(sentence) == expected_result:
        print 'Test_Case PASS'
    else:
        print "Test_Case FAIL"
