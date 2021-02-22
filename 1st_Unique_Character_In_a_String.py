def firstUniqueChar(s: str):
    #set_s = set(s)
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1

print(firstUniqueChar("leetcode"))




