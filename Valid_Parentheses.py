def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return 0
    else:
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        if s[0] in close_brackets or s[-1] in open_brackets:
            return 0
        res = []
        for i in s:
            if len(res) == 0:
                res.append(i)
            else:
                if i in open_brackets:
                    res.append(i)
                else:
                    last_open = res[-1]
                    if ((last_open == '[' and i == ']')
                        or (last_open == '(' and i == ')')
                        or (last_open == '{' and i == '}')):
                        del res[-1]
                    else:
                        return 0
        if len(res) > 0:
            return 0
        else:
            return 1

print(isValid("{[]}"))
