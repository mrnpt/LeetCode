def longestCommonPrefix(strs):
    if(all(v == '' for v in strs)):
        return ''
    res = ''
    for i in list(zip(*strs)):
        if i.count(i[0]) == len(i):
            res += i[0]
        else:
            break
    return res

print(longestCommonPrefix(["flower","flow","flight"]))
