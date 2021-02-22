import string


def reverse(x: int) -> int:
    strip_zeros_x = 0
    if x % 10 == 0:
        while abs(x) > 0:
            if x % 10 == 0:
                strip_zeros_x = x//10
                x = x // 10
            else:
                break;
    else:
        strip_zeros_x = x
    str_x = str(strip_zeros_x)
    if str_x[0] == '-':
        str_x = "-" + str_x[:0:-1]
    else:
        str_x = str_x[::-1]
    if int(str_x) not in range(-2**31, 2**31):
        return 0
    return str_x

print(reverse(1534236469))