def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    
    midpoint = (len(list))//2 # need to calculate midpoint everytime after min or max changes
    if list[midpoint] == target:
        return True
    elif list[midpoint] <= target:
        return recursive_binary_search(list[midpoint+1:], target)
    elif list[midpoint] >= target:
        return recursive_binary_search(list[:midpoint], target)
    return "Not found"

list = [1, 2, 3, 5, 8, 12, 23, 54, 89]
target = 12

print(recursive_binary_search(list,target))
# In a recursive binary search; returning index is hard since 
# everytime you are calling the function again with the spliced 
# list the index of the numbers change and in the end when the number
# matches it will always be at index 0.
# Hence only True or False.