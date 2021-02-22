from typing import List


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        a = nums[0]
        b = nums[0]
        for i in range(1, len(nums)):
            a = max(nums[i], a+nums[i])
            b = max(b, a)
    return b



print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))