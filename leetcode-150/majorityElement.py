def majorityElement(nums):
    i = 0
    threshold = int(len(nums)/2)
    if threshold == 0:
        return nums[0]
    freq = 0
    nums.sort()
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            freq += 1
        if freq > threshold-1:
            return nums[i]
        if nums[i] != nums[i+1]:
            freq = 0
        i += 1

def majorityElementdiff(nums): ## not mine but genius
        nums.sort()
        n = len(nums)
        return nums[n//2]

nums = [1]
print(majorityElementdiff(nums))