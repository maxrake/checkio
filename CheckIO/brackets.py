def checkio(expression):
    """Check expression for correctly matched brackets."""
    stack = []
    closers = dict(zip(')]}', '([{'))

    for char in expression:
        # build up the stack with opening brackets
        if char in '([{':
            stack.append(char)
        # tear down the stack when closing brackets are encountered
        if char in closers:
            if stack and stack[-1] == closers[char]:
                stack.pop()
            else:
                return False
    
    # check for remaining un-matched opening brackets
    return False if stack else True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print(" [+] All asserts passed.")
