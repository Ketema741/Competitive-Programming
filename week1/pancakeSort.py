class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        ans = []
        for i in range(l):
            cur_max = max(arr[0:l-i])
            index = arr.index(cur_max)
            if index == l-i-1:
                continue
            arr[:index+1] == reversed(arr[:index+1])
            ans.append(index+1)
            arr[:l-i] = reversed(arr[:l-i])
            ans.append(l-i)
        return ans
        