def isHappy(n):
    a = 0
    seen = set()
    while n > 0:
        a += (n%10)**2
        if (n//10) == 0:
            s = str(a)
            if s.count('1') == 1 and s.count('0') == len(s)-1:
                return True
            if a not in seen:
                seen.add(a)
            else:
                return False
            n = a
            a = 0
            continue
        n = n//10
    #return False

print(isHappy(2))