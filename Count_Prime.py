import math
from itertools import count
import sympy


def countPrime(n):
    res = 0
    for i in range(0, n):
        if i <= 1:
            continue
        if i <= 3:
            res += 1
        if i % 2 == 0 or i % 3 == 0:
            continue
        for j in range(2, (i//2)+1):
            if i % j == 0:
                break
            if j == (i//2):
                res += 1
    return res


# print(countPrime(10000))
import cProfile
cProfile.run("countPrime(499979)")