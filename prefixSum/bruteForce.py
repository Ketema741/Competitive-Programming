def maxArea(height):
    ans = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area  = (j-i) * min(height[i], height[j])
            ans = max(ans, area)
    return ans
# brute force approach
x = [1,8,6,2,5,4,8,3,7]
"""
    start with largest width
    left pointer and right pointer 
    each time calculate area store largest one 
"""

print(maxArea(x))