## Logarithmic time and constant space
# list needs to be a sorted one. 
# we are assuming the list is ascending in the code below.
def binary_search(list, target):
    min = 0
    max = len(list) - 1 # -1 because max will be used as index in the list
    
    while min <= max:
        midpoint = (min+max)//2 # need to calculate midpoint everytime after min or max changes
        if list[midpoint] == target:
            return midpoint 
        elif list[midpoint] < target:
            min = midpoint+1
        else:
            max = midpoint-1
    return "Not found"

list = [1, 2, 3, 5, 8, 12, 23, 54, 89]
target = 12

print(binary_search(list,target))


    
