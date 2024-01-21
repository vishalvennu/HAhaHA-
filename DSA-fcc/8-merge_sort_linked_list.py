import random
from linked_list import linkedList

def merge_sort(nums):
    if nums.length() == 1:
        return nums
    
    left_nums, right_nums = split(nums)
    left = merge_sort(left_nums)
    right = merge_sort(right_nums)

    merge(left, right)

def split(nums) -> [list, list]:
    mid = nums.length//2

    
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



l = linkedList()

for i in range(0,10):
    random_number = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
    l.add(random_number)

