def isPalindrome(s):
    tmp = ""
    for i in s:
        if i.isalpha() or i.isnumeric():
            tmp += i.lower()
    a = len(tmp)
    if a <= 1:
        return True
    if a % 2 == 0:
        b = tmp[a:(a//2)-1:-1]
    else:
        b = tmp[a:(a//2):-1]
    c = tmp[:a//2]
    return c == b

print(isPalindrome("a"))