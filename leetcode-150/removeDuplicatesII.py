## Remove Duplicates from Sorted Array II

def removeDuplicates(nums):
    i = 0
    flag = True
    while i < len(nums)-1:
        if(nums[i] == nums[i+1]) and flag == True:
            flag = False
        elif(nums[i] == nums[i+1]) and flag == False:
            nums.pop(i)
            i -= 1
        else:
            flag = True
        i += 1
    return nums

def removeDuplicatesdiff(nums):
    i = 0
    flag = True
    while i < len(nums)-1:
        if(nums[i] == nums[i+1]):
            if flag == True:
                flag = False
            else:
                nums.pop(i)
                i -= 1 
        else:
            flag = True
        i += 1
    return nums

nums = [1,1,1,4,2,2,2,5,6,3,3]
print(removeDuplicates(nums))