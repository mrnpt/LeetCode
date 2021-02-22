import math
from math import floor


def addBinary(a: str, b: str):
    # if a == "0":
    #     return b
    # if b == "0":
    #     return a
    a = int(a,2)
    b = int(b,2)
    #c = oct(a) + oct(b)
    return bin(a+b)[2:], a+b


print(addBinary("0", "0"))


