# better than a linear sort.

def merge_sort(nums) -> list:
    if len(nums) == 1:
        return nums
    
    left_nums, right_nums = split(nums)
    left = merge_sort(left_nums) # recursive calls take more memory.
    right = merge_sort(right_nums)

    return merge(left, right)

def split(nums) -> [list, list]:
    mid = len(nums)//2
    return nums[:mid], nums[mid:]

def merge(left, right) -> list:
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right): # linear time
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
    
    while i < len(left):
        result.append(left[i]) # linear time
        i += 1

    while j < len(right):
        result.append(right[j]) # linear time
        j += 1
    
    return result

nums = [5,4,3,2,4,5,6,3,1,2,6,6,8,3]
print(len(nums))
x = merge_sort(nums)
print(x)
print(len(x))
    

    
            