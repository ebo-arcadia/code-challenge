# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should
# return true if the string is valid, and false if it's invalid.

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# pseudocode
# opening = "{[("
# closing = "}])"
# define valid
# valid braces in dict = { ')': '(',
#                              '}': '{',
#                              ']': '['
#                              }
# iterate the string of braces
# if valid return true
# else return false
import collections


def valid_braces(string):
    # if the length of string is not even, it is valid
    if len(string) % 2:
        return False

    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


def valid_braces_2(string):
    # optimization for inputs that don't have an even number of elements
    if len(string) % 2:
        return False

    # mapping of opening and closing tokens
    tokens = {"(": ")", '{': '}', '[': ']'}
    # this data structure is faster than list when appending and removing from the end
    stack = collections.deque()

    for i in string:
        # if it's an opening token
        if i in tokens:
            # stack the corresponding closing token
            stack.append(tokens[i])
        # otherwise, it must be a closing token and, in this case
        # if the stack is empty or its top element doesn't match the current token
        # the token parity is invalid
        elif not stack or stack.pop() != i:
            return False

    # if at the end we have an empty stack, it means that the string is valid
    return not stack


def valid_braces_clever(string):
    while '{}' in string or '()' in string or '[]' in string:
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        string = string.replace('()', '')
    return string == ''


print(valid_braces("("))
print(valid_braces("}"))
print(valid_braces("()"))
print(valid_braces("(}"))
print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("[(])"))
print(valid_braces("[({})](]"))

print("testing cases for valid braces 2")
print(valid_braces_2("("))
print(valid_braces_2("}"))
print(valid_braces_2("()"))
print(valid_braces_2("(}"))
print(valid_braces_2("(){}[]"))
print(valid_braces_2("([{}])"))
print(valid_braces_2("[(])"))
print(valid_braces_2("[({})](]"))

print("testing cases for valid braces clever")
print(valid_braces_clever("("))
print(valid_braces_clever("}"))
print(valid_braces_clever("()"))
print(valid_braces_clever("(}"))
print(valid_braces_clever("(){}[]"))
print(valid_braces_clever("([{}])"))
print(valid_braces_clever("[(])"))
print(valid_braces_clever("[({})](]"))
