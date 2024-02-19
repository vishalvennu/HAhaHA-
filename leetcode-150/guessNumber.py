def guessNumber(n, pick):
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        if len(nums) == 1:
            return nums[0]

        x = 0
        y = len(nums)-1

        while x <= y:
            mid = (x+y)//2
            if pick == nums[mid]:
                return mid
            elif pick > nums[mid]:
                x = mid + 1
            else:
                y = mid - 1

            # result = guess(nums[mid])
            # if result == 0:
            #     return nums[mid]
            # elif result == 1:
            #     x = mid+1
            # else:
            #     y = mid-1

print(guessNumber(2126753390, 1702766719))
# print(guessNumber(45, 3))