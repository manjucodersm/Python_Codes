'''
Example:
{}[]() = True
{[}] = False'''


def valiidBraces(string):
    if not (string.count('(') == string.count(')') and
            string.count('[') == string.count(']') and
            string.count('{') == string.count('}')):
        return False
    
    stack = []
    dic = {')':'(', ']':'[', '}':'{'}
    
    for brace in string:
        stack.append(brace)
        if brace in ')]}':
            if not dic[brace] in stack:
                return False
            
            if not stack[stack.index(brace)-1] == dic[brace]:
                return False
            
            stack.remove(brace)
            del stack[stack.index(dic[brace])]
    
    if not stack:
        return True
    return False


if __name__ == '__main__':
    string = 'Success'
    if validBraces(string):
        print "Test-Case PASS"
    else:
        print "Test-Case FAIL"
