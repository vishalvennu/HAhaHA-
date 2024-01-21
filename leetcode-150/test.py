# using Merge Sort
def sortX(xlist):
    if len(xlist) == 1:
        return xlist
    leftX, rightX = split(xlist)
    left = sortX(leftX)
    right = sortX(rightX)

    return merge(left, right)

def split(xlist):
    mid= len(xlist)//2
    return xlist[:mid], xlist[mid:]

def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) & j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1

    return result