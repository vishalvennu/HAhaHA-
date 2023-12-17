def mergeSortedArray(nums1, nums2, m, n):
    nums1 = nums1[:m] + nums2
    nums1.sort()
    return nums1

def mergeSortedArray2(nums1, nums2, m, n): # append while you sort
    k = m+n-1 # len nums1
    i = m-1 #nums1
    j = n-1 #nums2

    while j>=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    return nums1

nums1 = [1,2,4,0,0,0]
nums2 = [3,5,6]
m = 3
n = 3

print(mergeSortedArray2(nums1, nums2, m, n))
