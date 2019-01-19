from stackLib import stack


def bc(string):
    if type(string) != str:
        s = str(string)
    else:
        s = string
    left = "({["
    right = "]})"
    checker = stack()
    check_right = True
    for i in range(0, len(s), 1):
        check_right = True
        for j in left:
            if s[i] == j:
                checker.push(s[i])
                check_right = False
                break  # break the for-loop to save on a few possible extra iterations
        if check_right:  # boolean toggle to avoid running unnecessary for-loop
            for k in right:
                if s[i] == k:
                    if len(checker.items) != 0:
                        compare = checker.pop()
                        if compare == "(":
                            compare = ")"
                        elif compare == "{":
                            compare = "}"
                        elif compare == "[":
                            compare = "]"
                        if compare != s[i]:
                            return [False, i]
                    else:
                        return [False, i]
    if len(checker.items) == 0:
        return [True, 0]  # made the choice to return 0 for true since it wasn't indicated in the lab
    else:
        return [False, i]
