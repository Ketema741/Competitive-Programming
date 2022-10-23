from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    left, right = 0, k
    res = 0     
    while right < len(arr):
        if (sum(arr[left:right]) / k) >= threshold:
            res += 1
        left += 1
        right += 1
    return res 