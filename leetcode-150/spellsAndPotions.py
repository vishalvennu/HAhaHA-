def successfulPairs(spells, potions, success):
    m = len(potions)
    potions.sort()

    for s in spells:
        i = 0
        j = m-1
        ll = 0
        result = []
        while i <= j:
            mid = (i + j)//2
            if s * potions[mid] >= success:
                j = mid - 1
                ll = mid
            else:
                i = mid + 1
        ll = len(potions)-ll
        result.append(ll)
    
    return result

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

print(successfulPairs(spells, potions, success))

# potions.sort()
# potion_len = len(potions)
# check_spells = list(set(spells))
# check_spells.sort()
# log = {}
# j = potion_len - 1
# for i in check_spells:
#     while j >= 0 and potions[j] * i >= success:
#         j -= 1
#     log[i] = potion_len - j - 1
# res = [log[i] for i in spells]
# return (res)