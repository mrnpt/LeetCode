from typing import List


def removeElement(nums: List[int], val: int):
    i = 0
    while val in nums:
        i += 1
        nums.remove(val)
    return nums, len(nums)
    # i = 0
    # for j in range(0, len(nums)):
    #     if nums[j] != val:
    #         nums[i] = nums[j]
    #         i += 1
    # return nums , i
    # if len(nums) == 0:
    #     return 0
    # i = 0
    # j = 0
    # while j < len(nums):
    #     if nums[j] != val:
    #         i += 1
    #         j += 1
    #     else:
    #         x = j
    #         while x < len(nums):
    #             if nums[x] != val:
    #                 nums[i], nums[x] = nums[x], nums[i]
    #                 i += 1
    #             x += 1
    #         j = x
    # return nums, i

print(removeElement([0,1,2,2,3,0,4,2], 2))