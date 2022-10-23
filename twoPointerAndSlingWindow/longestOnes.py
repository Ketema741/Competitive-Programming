from typing import List
def longestOnes(nums: List[int], k: int) -> int:
    res = 0
    left = 0
    
    for right in range(len(nums)):
        print(f"left:{left}, right = {right}, k = {k}")
        print(nums[left:right+1])
        if nums[right] == 0:
            k -= 1
        if k < 0:
            res = max(res, right - left )
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left + 1
longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)