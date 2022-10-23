def minimumPositive(nums):
    prefixSum = 0
    for i in range(len(nums)):
        prefixSum += nums[i]
        nums[i] = prefixSum
        
    minNum = min(nums)
    if minNum < 0: return 1 + (-minNum)
    else: return 1

print(minimumPositive([-3, 2, -3, 4, 2]))
    