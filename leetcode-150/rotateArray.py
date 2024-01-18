def rotateArray(nums, k): # better
    n = len(nums)
    if n > k+1:
        # print(nums)
        nums = nums[n-k:n] + nums[:n-k]
        return nums
    else:
        k = k-n
        nums = nums[n-k:n] + nums[:n-k]
        return nums

def rotateArray2(nums,k):
    # n=len(nums)
    a = []
    for i in range(k):
        temp = nums.pop()
        a.append(temp)
        nums = a + nums
        a.pop()
    return(nums)

        
    

nums = [1,2,3,4,5,6,7]
k = 3
print(rotateArray(nums,k))