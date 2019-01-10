from stackLib import Stack

def bc(u):
    b = Stack()
    pos = 0
    leftBraces = ['[', '(', '{']
    rightBraces = [']', ')', '}']
    for char in u:
        pos = pos + 1
        if char_in_set(char, leftBraces):
            b.push(char)
        elif char_in_set(char, rightBraces):
            if b.pop() != get_opening_brace(char):
                return [False, pos]
    if b.pop() != False:
        return [False, pos]
    return [True, 0]
        
def char_in_set(u, set):
    for v in set:
        if u == v:
            return True
    return False

def get_opening_brace(u):
    if u == "]":
        return "["
    elif u == ")":
        return "("
    elif u == "}":
        return "{"
    else:
        return ""
