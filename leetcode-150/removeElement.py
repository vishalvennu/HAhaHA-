def removeElement(nums1, element):
    # i = 
    for i in range(len(nums1)-1):
        if nums1[i] == element:
            nums1.pop(i)
            i -= 1
    return nums1

def removeElement1(nums1, element): ## works
    i = 0 
    while i < len(nums1):
        if nums1[i] == element:
            nums1.pop(i)
            i -= 1
        i += 1
    return nums1



nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement1(nums, val))