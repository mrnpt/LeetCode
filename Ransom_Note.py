def canConstruct(ransomNote, magazine):
    arr_ransomNote = list(ransomNote)
    arr_magazine = list(magazine)
    for i in arr_ransomNote:
        if i  in arr_magazine:
            arr_magazine.remove(i)
        else:
            return False
    return True

print(canConstruct("aa", "aba"))