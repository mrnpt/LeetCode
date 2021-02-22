import math


def isPalindrome(x: int):
    if x == 0:
        return 1
    elif x < 0:
        return 0
    else:
        reserve_x = 0
        tmp = x
        while tmp > 0:
            reserve_x = reserve_x * 10 + (tmp % 10)
            tmp = tmp // 10
        return reserve_x == x

res = isPalindrome(1221)

print(res)