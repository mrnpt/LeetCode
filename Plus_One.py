from typing import List


def plusOne(digits: List[int]) -> List[int]:
    i = len(digits)-1
    while i >= 0:
        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            i -= 1
            if i < 0:
                digits.insert(0, 1)
        else:
            break
    return digits


print(plusOne([9,9]))