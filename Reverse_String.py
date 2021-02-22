def reverseString(s):
    n = len(s)//2
    for i in range(0, n):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

s = ["H","a","n","n","a","h"]

reverseString(s)

print(s)