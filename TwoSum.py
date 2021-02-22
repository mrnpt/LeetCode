from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for x in nums:
        for y in (nums[:nums.index(x)] + nums[nums.index(x)+1:]):
            if x + y == target:
                a = nums.index(x)
                b = nums.index(y)
                if a == b:
                    b = nums.index(y, a+1)
                return [a, b]
    # nums_sorted = sorted(nums)
    # res = []
    # tmp = [x for x in nums_sorted if x <= target]
    # for i in range(len(tmp) - 1, 0, -1):
    #     for j in range(0, i):
    #         if tmp[i] + tmp[j] == target:
    #             a = nums.index(tmp[j])
    #             b = nums.index(tmp[i])
    #             if a == b:
    #                 b = nums.index(tmp[i], a+1)
    #             res = [a, b]
    # return res

print(twoSum([3,2,4], 6))