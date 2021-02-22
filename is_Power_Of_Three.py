import math
def isPowerOfThree(n):
    n = abs(n)
    if n == 0:
        return False
    return 3**round(math.log(n,3))

print(isPowerOfThree(243))