def containsNearbyDuplicate(nums, k):
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i-k])
    return False
print(containsNearbyDuplicate())
# import cProfile
# cProfile.run("containsNearbyDuplicate([1,2,3,1], 3)")