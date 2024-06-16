def findPeakelement(nums):
    i = 1
    nums = [0] + nums
    nums.append(0)
    
    while i < len(nums):
        l = 0
        r = 0
        if nums[i] > nums[i-1]:
            l = 1
        if nums[i] > nums[i+1]:
            r = 1
        
        if l == 1 and r == 1:
            return i-1
        if r == 1:
            i += 2
        if r == 0:
            i += 1
    return 0

nums = [1,2,3,1]
print(findPeakelement(nums))
            
            
