from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    nums1[m:] = nums2
    nums1.sort()

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))