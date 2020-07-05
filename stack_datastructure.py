from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, element):
        self.container.append(element)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0


def is_balenced_brackets(string):
    bracket_matches = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    return_value = True
    for ch in string:
        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)
        if ch == ')' or ch == ']' or ch == '}':
            if stack.is_empty():
                return_value = False
                break
            if not stack.pop() == bracket_matches[ch]:
                return_value = False
                break
            
    return return_value

string = '[(])'
print(is_balenced_brackets(string))
