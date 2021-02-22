def singleNumber(nums) -> int:
    x = set(nums)
    for i in x:
        if nums.count(i) == 1:
            return i

print(singleNumber([1]))