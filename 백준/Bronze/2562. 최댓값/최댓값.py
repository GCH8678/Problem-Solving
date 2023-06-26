nums = [int(input()) for i in range(9)]
maxNum = 0
maxIndex = 0

for i in range(len(nums)):
    if maxNum < nums[i]:
        maxNum = nums[i]
        maxIndex = i+1
print(maxNum)
print(maxIndex)