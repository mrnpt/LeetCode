def hammingWeight(n):
    print(bin(n).count('1'))
    # a = bin(n)
    # c = 0
    # while '1' in a and len(a) > 0:
    #     if a[-1] == '1':
    #         c += 1
    #     a = a[:-1]
    # print(c)

hammingWeight(4294967293)