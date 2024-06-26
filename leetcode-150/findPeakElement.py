def findPeakElement(nums):
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid=(left+right)>>1
            if (mid==0 or nums[mid]>=nums[mid-1] ) and (mid==len(nums)-1 or nums[mid]>=nums[mid+1]) :
                return mid
            elif nums[mid]<=nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1


nums = [1,2,1,3,4,4]
print(findPeakElement(nums))