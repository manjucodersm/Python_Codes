'''Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') ==> igPay atinlay siay oolcay
pig_it('Hello world !') ==> elloHay orldway !'''


def pigIt(text):
    result = []
    for word in text.split():
        ch = word
        if word.isalnum():
            ch = word[1: ] + word[0] + 'ay'
        result.append(ch)
      
    return ' '.join(result)


if __name__ == '__main__':
    text = 'Pig latin is cool'
    if pigIt(text) == 'igPay atinlay siay oolcay':
        print 'PASS'
    else:
        print 'FAIL'    
