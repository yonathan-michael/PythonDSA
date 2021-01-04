# Balanced Brackets
# {}
# {}{}
# (({[]}))

# We iterate through the string. Opening brackets get pushed onto a stack.
# Everytime we process a closing bracket, we pop the most-recent opening
# bracket from the stack. If it is a match, we move on. If the stack gets
# cleared, meaning all the opening brackets get popped until the stack is empty,
# then we have a string with balanced brackets.

from Stack.stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print("String : (((({}))))} Balanced or not?")
print(is_paren_balanced("(((({}))))"))