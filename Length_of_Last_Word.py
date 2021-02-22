def lengthOfLastWord(s: str):
    s = s.split()
    if len(s) == 0:
        return 0
    else:
        return len(s[-1])

print(lengthOfLastWord("Hello World"))